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

drivers = Driver.objects.all()
transports = Transport.objects.all()
clients = Passenger.objects.all()
statuses = [Status.objects.get(status_name="Success"),
            Status.objects.get(status_name="Failed")]
for i in range(5):
    
    for driver in drivers:
        for transport in transports:
            session = DriveSession(driver_id=driver,
                                   tr_id=transport,
                                   start_time=int(time.time()-10000),
                                   is_continues=False,
                                   end_time=int(time.time()))
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
                for i in range(rnd.randint(1,4)):
                    tran = Transaction(client_id=client,
                                        session_id=session,
                                        value=rnd.randint(-100, 100),
                                        time=int(time.time()) -86400*j + rnd.randint(36000),
                                        transaction_id=(i*10000 ) + rnd.randint(0, 10000000),
                                        status=statuses[rnd.randint(0, 1)]
                                        )
                    tran.save()


make_transactions()
