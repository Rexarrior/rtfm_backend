import rtfm.settings as my_settings
from django.conf import settings
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rtfm.settings')
django.setup()

from django.conf import settings
from core.models import *
import random as rnd
import time


def make_sessions():
    drivers = Driver.objects.all()
    transports = Transport.objects.all()
    clients = Passenger.objects.all()
    statuses = [Status.objects.get(status_name="Success"),
                Status.objects.get(status_name="Failed")]
    traces = Trace.objects.all()
    for driver in drivers:
            for i in range(15):
                trace = rnd.choice(traces)
                session = DriveSession(driver_id=driver,
                                        tr_id=rnd.choice(transports),
                                        start_time=int(time.time()-86000*i),
                                        is_continues=False,
                                        end_time=int(time.time()), 
                                        trace_id=trace)
                session.save()


def make_active_session():
    drivers = Driver.objects.all()
    transports = Transport.objects.all()
    clients = Passenger.objects.all()
    statuses = [Status.objects.get(status_name="Success"),
                Status.objects.get(status_name="Failed")]
    traces = Trace.objects.all()
    driver = rnd.choice(drivers)
    transport = rnd.choice(transports)
    trace = rnd.choice(traces)
    session = DriveSession(driver_id=driver, tr_id=transport,
                           trace_id=trace, start_time=int(time.time()),
                           is_continues=True
                           )
    print(session)
    session.save()
    

def make_transactions():
    drivers = Driver.objects.all()
    transports = Transport.objects.all()
    clients = Passenger.objects.all()
    statuses = [Status.objects.get(status_name="Success"),
                Status.objects.get(status_name="Failed")]
    sessions = DriveSession.objects.all()
    for session in sessions:
        for client in clients:
            for j in range(10):
                for i in range(rnd.randint(1, 4)):
                    value = session.trace_id.cost
                    time = session.start_time - 86400 * j +\
                                   rnd.randint(0, 36000)
                    tran_id = (i * 10000) + rnd.randint(0, 10000000)
                    tran = Transaction(client_id=client,
                                       session_id=session,
                                       value=value,
                                       time=time,
                                       transaction_id=tran_id,
                                       status=statuses[rnd.randint(0, 1)]
                                       )
                    tran.save()


def erase_sessions_and_transactions():
    DriveSession.objects.all().delete()
    Transaction.objects.all().delete()

erase_sessions_and_transactions()
make_sessions()
make_transactions()
make_active_session()
