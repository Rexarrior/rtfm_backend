# Generated by Django 2.1.2 on 2019-06-08 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190608_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drivesession',
            name='driver_id',
        ),
        migrations.RemoveField(
            model_name='drivesession',
            name='tr_id',
        ),
        migrations.DeleteModel(
            name='Trace',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='client_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='session_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='status',
        ),
        migrations.RemoveField(
            model_name='transport',
            name='transportType',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='DriveSession',
        ),
        migrations.DeleteModel(
            name='Passenger',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='Transport',
        ),
        migrations.DeleteModel(
            name='TransportType',
        ),
    ]
