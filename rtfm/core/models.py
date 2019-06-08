from django.db import models as models
from pb_model.models import ProtoBufMixin
from core.proto_models import db_models_pb2 as proto


class Passenger(models.Model):
    pb_model = proto.Passenger
    client_id = models.IntegerField()
    is_validated = models.IntegerField()
    balance = models.FloatField()
    fid_card = models.IntegerField()
    register_date = models.PositiveIntegerField()
 

class Driver(models.Model):
    pb_model = proto.Driver
    driver_id = models.IntegerField()


class DriveSession(models.Model):
    pb_model = proto.DriveSession
    session_id = models.IntegerField()
    driver_id = models.IntegerField()
    transport_id = models.IntegerField()
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    

class Transport(models.Model):
    pb_model = proto.Transport
    tr_id = models.IntegerField()


class Transaction( models.Model):
    pb_model = proto.Transaction
    client_id = models.IntegerField()
    session_id = models.IntegerField()
    value = models.FloatField()
    time = models.PositiveIntegerField()


class Trace(models.Model):
    pb_model = proto.Trace
    trace_id = models.IntegerField()
    cost = models.FloatField()

