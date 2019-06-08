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

transportTypeMap ={
    'Bus': ('Bus', 0),
    'МТ': ('МТ', 1),
    'Taxy': ('Taxy', 2),
    'Subway': ('Subway', 3),
}

payStatusMap = {
    'Available':0,
    'Blocked':1,
}

@require_http_methods(["GET"])
def open_session(request):
    try:
        driver_id = request.META['driver_id']
        transport_id = request.META['transport_id']
        trace_id = request.META['trace_id']
        start_time = int(time.time())
        session = DriveSession(driver_id=driver_id, tr_id=transport_id,
                               trace_id=trace_id, start_time=start_time,
                               is_continues=True)
        session.save()
    except KeyError:
        return HttpResponseBadRequest()
    return HttpResponse()


@require_http_methods(["GET"])
def close_session(request):
    try:
        session_id = request.META['session_id']
        session = DriveSession.objects.get(session_id=session_id)
        session.is_continues = False
        session.end_time = int(time.time())
        session.save()
    except DriveSession.DoesNotExist:
        return HttpResponseBadRequest()
    except KeyError:
        return HttpResponseBadRequest()
    return HttpResponse()


@require_http_methods(["GET"])
def get_valid_list(request):
    try:
        query = Passenger.objects.all()
        ret = {q['client_id']: q['is_validate'] for q in query}
        proto_ret = other_proto.ClientValidationList()
        proto_ret.Clients.update(ret)
        return HttpResponse(status=200, content=proto_ret.SerializeToString())
    except KeyError:
        return HttpResponseBadRequest()


@require_http_methods(["POST"])
def transact(request):
    try:
        proto_paiment = other_proto.Payment()
        proto_paiment.FromString(request.body)
        if (Transaction.objects.filter(transaction_id=proto_paiment.TransactionID).exists()):
            return HttpResponse(status=200)

        session = DriveSession.objects.get(tr_id=proto_paiment.TransportID,
                                           is_continues=True)
        value = Trace.objects.get(trace_id=session.trace_id).cost
        transaction = Transaction(client_id=proto_paiment.ClientID,
                                  session_id=session.session_id,
                                  value=value,
                                  time=int(time.time()),
                                  transaction_id=proto_paiment.TransactionID)
        if (not transaction.client_id is None):
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
    print('stage 1')
    try:
        proto_request = other_proto.RecentPaymentsRequest()
        proto_request.FromString(request.body)
        print(f'body: {request.body}')
        client_id = proto_request.client_id
        print(f'client_id = {client_id}')
        transactions = Transaction.objects.filter(client_id=client_id,
                                                  ).order_by('-time')
        resp = other_proto.RecentPaymentsResponce()
        print(f'start forming responce. Transactions count={len(transactions)}')
        for tran in transactions:
            session = DriveSession.objects.get(session_id=tran.session_id)
            transport = Transport.objects.get(tr_id=session.tr_id)
            trace = Trace.objects.get(trace_id=session.trace_id)
            completed_payment = other_proto.CompletedPayment()
            completed_payment.date = tran.time
            completed_payment.id = tran.transaction_id
            completed_payment.status = statusMap[tran.status][1]
            completed_payment.type = transportTypeMap[transport.type]
            completed_payment.title = trace.title
            completed_payment.price = f'{int(trace.cost / 100)} руб. {trace.cost % 100} коп.'
            resp.Payments.add(completed_payment)
            print(f'{completed_payment.id} added to responce')
        print('responce formed')
        s = resp.SerializeToString()
        print(f'responce content {s}')
        return HttpResponse()
    except KeyError:
        return HttpResponseBadRequest()
              
    
def user_info(request):
    req = other_proto.UserInfoRequest()
    req.FromString(request)
    client = Passenger.objects.get(client_id=req.client_id)
    res = other_proto.UserInfoResponse()
    if client.is_validated: 
        res.status = payStatusMap['Available']
    else:
        res.status = payStatusMap['Blocked']
    res.balance = f'{int(trace.cost / 100)} руб. {trace.cost % 100} коп.'  
    return HttpResponse(status=200, content=res.SerializeToString())