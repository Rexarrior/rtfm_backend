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
    p = Passenger(is_validated=True, balance=rnd.randint(0, 100000),
                  register_date=rnd.randint(1000000, 3000000),
                  fid_card=rnd.randint(10000, 10000000))
    p.save()

for i in range(10):
    t = Trace(cost=500*rnd.randint(3, 25),
              title=f'Маршрут № {rnd.randint(10, 100)}')
    t.save()


T = TransportType(transport_type="Bus")
T.save()

T = TransportType(transport_type="МТ")
T.save()
T = TransportType(transport_type="Taxy")
T.save()
T = TransportType(transport_type="Subway")
T.save()
tr_types = TransportType.objects.all()
for i in range(10):
    t = Transport(transportType=rnd.choice(tr_types))
    t.save()

S = Status(status_name="Success")
S.save()

S = Status(status_name="Failed")
S.save()

d = Driver()
d.save()