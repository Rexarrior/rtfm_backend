import rtfm.settings as my_settings
from django.conf import settings
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rtfm.settings')
django.setup()
import datetime
from core.models import *


with open('report.csv', 'wt', encoding='utf-8') as f:
    f.write('Название маршрута;Дата;Период сессии; Пассажиропоток;\n')
    traces = Trace.objects.all()
    for trace in traces:
        sessions = DriveSession.objects.filter(trace_id=trace).filter(is_continues=False)
        for session in sessions:
            start_time = datetime.datetime.fromtimestamp(session.start_time)
            end_time = datetime.datetime.fromtimestamp(session.end_time)
            count = len(Transaction.objects.filter(session_id=session))
            date = start_time.strftime('%Y-%m-%d')
            start_time = start_time.strftime('%H:%M')
            end_time = end_time.strftime('%H:%M')
            timestring = f'{start_time} - {end_time}'
            f.write(f'{trace.title};{date};{timestring};{count}\n')