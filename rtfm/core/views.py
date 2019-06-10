from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest,\
                        HttpResponseForbidden, HttpResponseNotFound,\
                        FileResponse
from django.views.decorators.http import require_http_methods

from core.models import *
import time
import json
import os
import core.proto_models.other_models_pb2 as other_proto
from rtfm.settings import BASE_DIR
CLIENT_MIN_BALANCE = 0

statusMap = {
    'Success': (Status.objects.get(status_name='Success'), 0),
    'Failed': (Status.objects.get(status_name='Failed'), 1)
}

transportTypeMap = {
    'Bus': (TransportType.objects.get(transport_type='Bus'), 0),
    'МТ': (TransportType.objects.get(transport_type='МТ'), 1),
    'Taxy': (TransportType.objects.get(transport_type='Taxy'), 2),
    'Subway': (TransportType.objects.get(transport_type='Subway'), 3),
}

payStatusMap = {
    'Available': 0,
    'Blocked': 1,
}


def make_str_from_price(price):
    return f'{int(price / 100)} руб. {int(price % 100)} коп.'


def apply_payment(payment):
    if (not Transaction.objects.filter(transaction_id=payment.TransactionID).\
            exists()):
        session = DriveSession.objects.get(tr_id=payment.TransportID,
                                           is_continues=True)
        value = -session.trace_id.cost
        client = Passenger.objects.get(client_id=payment.ClientID)
        transaction = Transaction(client_id=client,
                                  session_id=session,
                                  value=value,
                                  time=int(time.time()),
                                  transaction_id=payment.TransactionID)
        print(f'client id {transaction.client_id}')                                  
        if (transaction.client_id is not None):
            client = transaction.client_id
            if (not client.is_validated):
                print('client is not validated')
                transaction.status = statusMap['Failed'][0]
                transaction.save()
                return HttpResponseForbidden()
            print(f'client balance changed for {transaction.value}')
            client.balance += transaction.value
            if client.balance < CLIENT_MIN_BALANCE:
                client.is_validated = False
            client.save()
        transaction.status = statusMap['Success'][0]
        transaction.save()
    return HttpResponse()


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
        req = req.FromString(request.body)
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
        ret = {q.client_id: q.is_validated for q in query}
        proto_ret = other_proto.ClientValidationList()
        proto_ret.Clients.update(ret)
        return HttpResponse(proto_ret.SerializeToString())
    except KeyError:
        return HttpResponseBadRequest()


def transact(request):
    try:
        proto_paiment = other_proto.Payment()
        proto_paiment = proto_paiment.FromString(request.body)
        return apply_payment(proto_paiment)
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
    print(f'id: {client_id};  len: {len(transactions)};')
    for tran in transactions:
        resp.Payments.add()        
        session = tran.session_id
        transport = session.tr_id
        trace = session.trace_id
        taxy_type = TransportType.objects.get(transport_type='Taxy')
        title = trace.title
        if (transport.transportType == taxy_type):
            title = "Такси"
        resp.Payments[i].date = tran.time
        resp.Payments[i].id = tran.transaction_id
        resp.Payments[i].status = statusMap[tran.status.status_name][1]
        resp.Payments[i].type = transportTypeMap[transport.transportType.transport_type][1]
        resp.Payments[i].title = title
        resp.Payments[i].price = make_str_from_price(trace.cost)
        i += 1
    s = resp.SerializeToString()
    return HttpResponse(s)



def user_info(request):
    req = other_proto.UserInfoRequest()
    req = req.FromString(request.body)
    client = Passenger.objects.get(client_id=req.client_id)
    res = other_proto.UserInfoResponse()
    if client.is_validated: 
        res.status = payStatusMap['Available']
    else:
        res.status = payStatusMap['Blocked']
    res.balance = make_str_from_price(client.balance)
    return HttpResponse(res.SerializeToString())


def get_price(request):
    req = other_proto.GetPriceRequest()
    req = req.FromString(request.body)
    print(f'{req.transport_id}')
    session = DriveSession.objects.get(tr_id=req.transport_id,
                                       is_continues=True)
    value = session.trace_id.cost
    res = other_proto.GetPriceResponse()
    res.Price = make_str_from_price(value)
    res.session_id = session.session_id
    return HttpResponse(res.SerializeToString())


def index_page(request):
    return FileResponse(open(os.path.join(BASE_DIR,
                                          r".static/rtfm_front/index.html"),
                             'rb'))


def favicon(request):
    return FileResponse(open(os.path.join(BASE_DIR,
                                          r"static/rtfm_front/favicon.ico"),
                             'rb'))


def static_delivery(request, path=""):
    print(f"serve static {path}")
    if os.path.isfile(os.path.join(BASE_DIR, 'static/rtfm_front/resources/', path)):
        response = FileResponse(open(os.path.join(BASE_DIR,
                                     'static/rtfm_front/resources/',
                                     path), 'rb'))
        if 'css'in path:
            response['Content-Type'] = 'text/css'
        if 'js' in path:
            response['Content-Type'] = 'text/javascript'

    else:
        response = HttpResponseNotFound()
    return response



def sync_payments(request):
    req = other_proto.TransactionSyncRequest()
    req = req.FromString(request.body)
    for payment in req.Payments:
        apply_payment(payment)
    return HttpResponse()


def refil(request):
    req = other_proto.RefilRequest()
    req = req.FromString(request.body)
    client = Passenger.objects.get(client_id=req.client_id)
    client.balance += req.value
    if (client.balance > CLIENT_MIN_BALANCE):
        client.is_validated = True
    client.save()
    return HttpResponse()

def traffic_stats(request):
    req = other_proto.TrafficStatsRequest()
    req = req.FromString(request.body)
    trace = Trace.objects.get(trace_id = req.trace_id)
    sessions = DriveSession.objects.filter(trace_id = trace).filter(is_continues = False)
    res = other_proto.TrafficStatsResponce()
    i = 0
    for session in sessions:
        res.Stats.add()
        res.Stats[i].start_time = session.start_time
        res.Stats[i].end_time = session.end_time
        res.Stats[i].count = len(Transaction.objects.filter(session_id = session))
        i += 1
    return HttpResponse(res.SerializeToString(res))