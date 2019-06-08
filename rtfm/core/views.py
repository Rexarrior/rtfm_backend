from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest,\
                        HttpResponseForbidden

from core.models import *
import time
import json
import core.proto_models.other_models_pb2 as other_proto
CLIENT_MIN_BALANCE = 0


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


def get_valid_list(request):
    try:
        query = Passenger.objects.all()
        ret = {q['client_id']: q['is_validate'] for q in query}
        proto_ret = other_proto.ClientValidationList()
        proto_ret.Clients.update(ret)
        return HttpResponse(status=200, content=proto_ret.SerializeToString())
    except KeyError:
        return HttpResponseBadRequest()


def transact(request):
    try:
        proto_trans = proto.Transaction()
        proto_trans.FromString(request.body)
        if (Transaction.objects.filter(transaction_id=proto_trans.transaction_id).exists()):
            return HttpResponse(status=200)
        
        transaction = Transaction(client_id=proto_trans.client_id,
                                  session_id=proto_trans.session_id,
                                  value=proto_trans.value,
                                  time=proto_trans.time,
                                  transaction_id=proto_trans.transaction_id)
        if (not transaction.client_id is None):
            client = Passenger.objects.get(client_id=transaction.client_id)
            if (not client.is_validate):
                return HttpResponseForbidden()
            
            client.balance += transaction.value
            if client.balance < CLIENT_MIN_BALANCE:
                client.is_validate = False
            client.save()
        transaction.save()
    except KeyError:
        return HttpResponseBadRequest()

    
