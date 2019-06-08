import rtfm.settings as my_settings
from django.conf import settings
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rtfm.settings')
django.setup()

from django.conf import settings
from core.models import *
import random as rnd

for i in range(3):
    p = Passenger(is_validated=True, balance=rnd.randint(0, 1000), register_date=rnd.randint(1000000, 3000000), fid_card=rnd.randint(10000, 10000000))
    p.save()

t = Trace(cost=100, title='Маршрут № 40')
t.save()


T = TransportType(transport_type="Bus")
T.save()
t = Transport(transportType=T)
t.save()
T = TransportType(transport_type="МТ")
T.save()
T = TransportType(transport_type="Taxy")
T.save()
T = TransportType(transport_type="Subway")
T.save()

S = Status(status_name="Success")
S.save()

S = Status(status_name="Failed")
S.save()

d = Driver()
d.save()