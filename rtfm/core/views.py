from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest,\
                        HttpResponseForbidden
from django.views.decorators.http import require_http_methods

from core.models import *
import time
import json
import core.proto_models.other_models_pb2 as other_proto
CLIENT_MIN_BALANCE = 0

statusMap = {
    'Success': ('Success', 0),
    'Failed': ('Failed', 1)
}

transportTypeMap = {
    'Bus': ('Bus', 0),
    'МТ': ('МТ', 1),
    'Taxy': ('Taxy', 2),
    'Subway': ('Subway', 3),
}

payStatusMap = {
    'Available': 0,
    'Blocked': 1,
}


def open_session(request):
    try:
        req = other_proto.SessionOpenRequest()
        req = req.FromString(request.body)
        start_time = int(time.time())
        driver = Driver.objects.get(driver_id=req.driver_id)
        transport = Transport.objects.get(tr_id=req.transport_id)
        trace = Trace.objects.get(trace_id=req.trace_id)
        session = DriveSession(driver_id=driver, tr_id=transport,
                               trace_id=trace, start_time=start_time,
                               is_continues=True)
        session.save()
        res = other_proto.SessionOpenResponce()
        res.session_id = session.session_id
        return HttpResponse(res.SerializeToString())
    except KeyError:
        return HttpResponseBadRequest()


def close_session(request):
    try:
        req = other_proto.SessionCloseRequest()
        req = req.FromString()
        session = DriveSession.objects.get(session_id=req.session_id)
        session.is_continues = False
        session.end_time = int(time.time())
        session.save()
        return HttpResponse()
    except DriveSession.DoesNotExist:
        return HttpResponseBadRequest()
    except KeyError:
        return HttpResponseBadRequest()
    return HttpResponse()


def get_valid_list(request):
    try:
        query = Passenger.objects.all()
        ret = {q['client_id']: q['is_validate'] for q in query}
        proto_ret = other_proto.ClientValidationList()
        proto_ret.Clients.update(ret)
        return HttpResponse(proto_ret.SerializeToString())
    except KeyError:
        return HttpResponseBadRequest()


@require_http_methods(["POST"])
def transact(request):
    try:
        proto_paiment = other_proto.Payment()
        proto_paiment = proto_paiment.FromString(request.body)
        if (Transaction.objects.filter(transaction_id=proto_paiment.TransactionID).exists()):
            return HttpResponse(status=200)

        session = DriveSession.objects.get(tr_id=proto_paiment.TransportID,
                                           is_continues=True)
        value = Trace.objects.get(trace_id=session.trace_id).cost
        client = Passenger.objects.get(client_id=proto_paiment.ClientID)
        transaction = Transaction(client_id=client,
                                  session_id=session
                                  value=value,
                                  time=int(time.time()),
                                  transaction_id=proto_paiment.TransactionID)
        if (transaction.client_id is not None):
            client = Passenger.objects.get(client_id=transaction.client_id)
            if (not client.is_validate):
                transaction.status = statusMap['Failed'][0]
                transaction.save()
                return HttpResponseForbidden()
            client.balance += transaction.value            
            if client.balance < CLIENT_MIN_BALANCE:
                client.is_validate = False
            client.save()
            transaction.status = statusMap['Success'][0]
            transaction.save()
    except KeyError:
        return HttpResponseBadRequest()


def recent_payments(request):
    proto_request = other_proto.RecentPaymentsRequest()
    proto_request = proto_request.FromString(request.body)
    client_id = proto_request.client_id
    transactions = Transaction.objects.filter(client_id=client_id,
                                                ).order_by('-time')
    resp = other_proto.RecentPaymentsResponce()
    i = 0
    for tran in transactions:
        resp.Payments.add()        
        session = tran.session_id
        transport = session.tr_id
        trace = session.trace_id
        resp.Payments[i].date = tran.time
        resp.Payments[i].id = tran.transaction_id
        resp.Payments[i].status = statusMap[tran.status.status_name][1]
        resp.Payments[i].type = transportTypeMap[transport.transportType.transport_type][1]
        resp.Payments[i].title = trace.title
        resp.Payments[i].price = f'{int(trace.cost / 100)} руб. {trace.cost % 100} коп.'
        i += 1
    s = resp.SerializeToString()
    return HttpResponse(s)



def user_info(request):
    req = other_proto.UserInfoRequest()
    req = req.FromString(request)
    client = Passenger.objects.get(client_id=req.client_id)
    res = other_proto.UserInfoResponse()
    if client.is_validated: 
        res.status = payStatusMap['Available']
    else:
        res.status = payStatusMap['Blocked']
    res.balance = f'{int(trace.cost / 100)} руб. {trace.cost % 100} коп.'
    return HttpResponse(res.SerializeToString())