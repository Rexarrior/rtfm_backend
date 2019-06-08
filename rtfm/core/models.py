from django.db import models as models
from core.proto_models import db_models_pb2 as proto


class Passenger(models.Model):
    client_id = models.AutoField(primary_key=True)
    is_validated = models.BooleanField()
    balance = models.IntegerField()
    fid_card = models.IntegerField()
    register_date = models.PositiveIntegerField()
 

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)


class DriveSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    driver_id = models.ForeignKey('Driver', 
                                  on_delete=models.CASCADE)
    tr_id = models.ForeignKey('Transport',
                              on_delete=models.CASCADE)
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    is_continues = models.BooleanField()
    

class TransportType(models.Model):
    transport_type = models.CharField(max_length=50)


class Transport(models.Model):
    tr_id = models.AutoField(primary_key=True)
    transportType = models.ForeignKey('TransportType',
                                      on_delete=models.CASCADE)


class Transaction(models.Model):
    client_id = models.ForeignKey('Passenger', 
                                  on_delete=models.CASCADE)
    session_id = models.ForeignKey('DriveSession', 
                                   on_delete=models.CASCADE)
    transaction_id = models.IntegerField(primary_key=True)
    value = models.IntegerField()
    time = models.PositiveIntegerField()
    status = models.ForeignKey('Status', on_delete=models.CASCADE)


class Trace(models.Model):
    trace_id = models.AutoField(primary_key=True)
    cost = models.FloatField()
    title = models.CharField(max_length=50)


class Status(models.Model):
    status_name = models.CharField(max_length=50)

