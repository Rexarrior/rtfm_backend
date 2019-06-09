# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: other_models.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import core.proto_models.db_models_pb2 as db__models__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='other_models.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12other_models.proto\x1a\x0f\x64\x62_models.proto\"{\n\x14\x43lientValidationList\x12\x33\n\x07\x43lients\x18\x01 \x03(\x0b\x32\".ClientValidationList.ClientsEntry\x1a.\n\x0c\x43lientsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"G\n\x07Payment\x12\x10\n\x08\x43lientID\x18\x01 \x01(\x03\x12\x15\n\rTransactionID\x18\x02 \x01(\x03\x12\x13\n\x0bTransportID\x18\x03 \x01(\x03\"\x81\x01\n\x10\x43ompletedPayment\x12\r\n\x05price\x18\x01 \x01(\t\x12\x1c\n\x04type\x18\x02 \x01(\x0e\x32\x0e.TransportType\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\x05\x12\n\n\x02id\x18\x05 \x01(\x03\x12\x17\n\x06status\x18\x06 \x01(\x0e\x32\x07.Status\"*\n\x15RecentPaymentsRequest\x12\x11\n\tclient_id\x18\x01 \x01(\x03\"=\n\x16RecentPaymentsResponce\x12#\n\x08Payments\x18\x01 \x03(\x0b\x32\x11.CompletedPayment\"$\n\x0fUserInfoRequest\x12\x11\n\tclient_id\x18\x01 \x01(\x03\"y\n\x10UserInfoResponse\x12+\n\x06status\x18\x01 \x01(\x0e\x32\x1b.UserInfoResponse.PayStatus\x12\x0f\n\x07\x62\x61lance\x18\x02 \x01(\t\"\'\n\tPayStatus\x12\r\n\tAvailable\x10\x00\x12\x0b\n\x07\x42locked\x10\x01\"O\n\x12SessionOpenRequest\x12\x11\n\tdriver_id\x18\x01 \x01(\x05\x12\x14\n\x0ctransport_id\x18\x02 \x01(\x05\x12\x10\n\x08trace_id\x18\x03 \x01(\x05\")\n\x13SessionOpenResponce\x12\x12\n\nsession_id\x18\x01 \x01(\x05\")\n\x13SessionCloseRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x05\"\'\n\x0fGetPriceRequest\x12\x14\n\x0ctransport_id\x18\x01 \x01(\x05\"!\n\x10GetPriceResponse\x12\r\n\x05Price\x18\x01 \x01(\t\"4\n\x16TransactionSyncRequest\x12\x1a\n\x08Payments\x18\x01 \x03(\x0b\x32\x08.Payment\"0\n\x0cRefilRequest\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05\"G\n\x10TrafficStatPoint\x12\x12\n\nstart_time\x18\x01 \x01(\r\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\r\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\"J\n\x14TrafficStatsResponce\x12\x10\n\x08trace_id\x18\x01 \x01(\x05\x12 \n\x05Stats\x18\x02 \x03(\x0b\x32\x11.TrafficStatPoint\"\'\n\x13TrafficStatsRequest\x12\x10\n\x08trace_id\x18\x01 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[db__models__pb2.DESCRIPTOR,])



_USERINFORESPONSE_PAYSTATUS = _descriptor.EnumDescriptor(
  name='PayStatus',
  full_name='UserInfoResponse.PayStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Available', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Blocked', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=596,
  serialized_end=635,
)
_sym_db.RegisterEnumDescriptor(_USERINFORESPONSE_PAYSTATUS)


_CLIENTVALIDATIONLIST_CLIENTSENTRY = _descriptor.Descriptor(
  name='ClientsEntry',
  full_name='ClientValidationList.ClientsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ClientValidationList.ClientsEntry.key', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ClientValidationList.ClientsEntry.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=162,
)

_CLIENTVALIDATIONLIST = _descriptor.Descriptor(
  name='ClientValidationList',
  full_name='ClientValidationList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Clients', full_name='ClientValidationList.Clients', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLIENTVALIDATIONLIST_CLIENTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=162,
)


_PAYMENT = _descriptor.Descriptor(
  name='Payment',
  full_name='Payment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ClientID', full_name='Payment.ClientID', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TransactionID', full_name='Payment.TransactionID', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TransportID', full_name='Payment.TransportID', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=235,
)


_COMPLETEDPAYMENT = _descriptor.Descriptor(
  name='CompletedPayment',
  full_name='CompletedPayment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='CompletedPayment.price', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='CompletedPayment.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='CompletedPayment.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='CompletedPayment.date', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='CompletedPayment.id', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='CompletedPayment.status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=367,
)


_RECENTPAYMENTSREQUEST = _descriptor.Descriptor(
  name='RecentPaymentsRequest',
  full_name='RecentPaymentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='RecentPaymentsRequest.client_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=411,
)


_RECENTPAYMENTSRESPONCE = _descriptor.Descriptor(
  name='RecentPaymentsResponce',
  full_name='RecentPaymentsResponce',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Payments', full_name='RecentPaymentsResponce.Payments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=474,
)


_USERINFOREQUEST = _descriptor.Descriptor(
  name='UserInfoRequest',
  full_name='UserInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='UserInfoRequest.client_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=476,
  serialized_end=512,
)


_USERINFORESPONSE = _descriptor.Descriptor(
  name='UserInfoResponse',
  full_name='UserInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='UserInfoResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balance', full_name='UserInfoResponse.balance', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USERINFORESPONSE_PAYSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=514,
  serialized_end=635,
)


_SESSIONOPENREQUEST = _descriptor.Descriptor(
  name='SessionOpenRequest',
  full_name='SessionOpenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='driver_id', full_name='SessionOpenRequest.driver_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transport_id', full_name='SessionOpenRequest.transport_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='SessionOpenRequest.trace_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=637,
  serialized_end=716,
)


_SESSIONOPENRESPONCE = _descriptor.Descriptor(
  name='SessionOpenResponce',
  full_name='SessionOpenResponce',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='SessionOpenResponce.session_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=718,
  serialized_end=759,
)


_SESSIONCLOSEREQUEST = _descriptor.Descriptor(
  name='SessionCloseRequest',
  full_name='SessionCloseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='SessionCloseRequest.session_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=761,
  serialized_end=802,
)


_GETPRICEREQUEST = _descriptor.Descriptor(
  name='GetPriceRequest',
  full_name='GetPriceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transport_id', full_name='GetPriceRequest.transport_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=804,
  serialized_end=843,
)


_GETPRICERESPONSE = _descriptor.Descriptor(
  name='GetPriceResponse',
  full_name='GetPriceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Price', full_name='GetPriceResponse.Price', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=845,
  serialized_end=878,
)


_TRANSACTIONSYNCREQUEST = _descriptor.Descriptor(
  name='TransactionSyncRequest',
  full_name='TransactionSyncRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Payments', full_name='TransactionSyncRequest.Payments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=880,
  serialized_end=932,
)


_REFILREQUEST = _descriptor.Descriptor(
  name='RefilRequest',
  full_name='RefilRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='RefilRequest.client_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='RefilRequest.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=934,
  serialized_end=982,
)


_TRAFFICSTATPOINT = _descriptor.Descriptor(
  name='TrafficStatPoint',
  full_name='TrafficStatPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='TrafficStatPoint.start_time', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='TrafficStatPoint.end_time', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='TrafficStatPoint.count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=984,
  serialized_end=1055,
)


_TRAFFICSTATSRESPONCE = _descriptor.Descriptor(
  name='TrafficStatsResponce',
  full_name='TrafficStatsResponce',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='TrafficStatsResponce.trace_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Stats', full_name='TrafficStatsResponce.Stats', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1057,
  serialized_end=1131,
)


_TRAFFICSTATSREQUEST = _descriptor.Descriptor(
  name='TrafficStatsRequest',
  full_name='TrafficStatsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='TrafficStatsRequest.trace_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1133,
  serialized_end=1172,
)

_CLIENTVALIDATIONLIST_CLIENTSENTRY.containing_type = _CLIENTVALIDATIONLIST
_CLIENTVALIDATIONLIST.fields_by_name['Clients'].message_type = _CLIENTVALIDATIONLIST_CLIENTSENTRY
_COMPLETEDPAYMENT.fields_by_name['type'].enum_type = db__models__pb2._TRANSPORTTYPE
_COMPLETEDPAYMENT.fields_by_name['status'].enum_type = db__models__pb2._STATUS
_RECENTPAYMENTSRESPONCE.fields_by_name['Payments'].message_type = _COMPLETEDPAYMENT
_USERINFORESPONSE.fields_by_name['status'].enum_type = _USERINFORESPONSE_PAYSTATUS
_USERINFORESPONSE_PAYSTATUS.containing_type = _USERINFORESPONSE
_TRANSACTIONSYNCREQUEST.fields_by_name['Payments'].message_type = _PAYMENT
_TRAFFICSTATSRESPONCE.fields_by_name['Stats'].message_type = _TRAFFICSTATPOINT
DESCRIPTOR.message_types_by_name['ClientValidationList'] = _CLIENTVALIDATIONLIST
DESCRIPTOR.message_types_by_name['Payment'] = _PAYMENT
DESCRIPTOR.message_types_by_name['CompletedPayment'] = _COMPLETEDPAYMENT
DESCRIPTOR.message_types_by_name['RecentPaymentsRequest'] = _RECENTPAYMENTSREQUEST
DESCRIPTOR.message_types_by_name['RecentPaymentsResponce'] = _RECENTPAYMENTSRESPONCE
DESCRIPTOR.message_types_by_name['UserInfoRequest'] = _USERINFOREQUEST
DESCRIPTOR.message_types_by_name['UserInfoResponse'] = _USERINFORESPONSE
DESCRIPTOR.message_types_by_name['SessionOpenRequest'] = _SESSIONOPENREQUEST
DESCRIPTOR.message_types_by_name['SessionOpenResponce'] = _SESSIONOPENRESPONCE
DESCRIPTOR.message_types_by_name['SessionCloseRequest'] = _SESSIONCLOSEREQUEST
DESCRIPTOR.message_types_by_name['GetPriceRequest'] = _GETPRICEREQUEST
DESCRIPTOR.message_types_by_name['GetPriceResponse'] = _GETPRICERESPONSE
DESCRIPTOR.message_types_by_name['TransactionSyncRequest'] = _TRANSACTIONSYNCREQUEST
DESCRIPTOR.message_types_by_name['RefilRequest'] = _REFILREQUEST
DESCRIPTOR.message_types_by_name['TrafficStatPoint'] = _TRAFFICSTATPOINT
DESCRIPTOR.message_types_by_name['TrafficStatsResponce'] = _TRAFFICSTATSRESPONCE
DESCRIPTOR.message_types_by_name['TrafficStatsRequest'] = _TRAFFICSTATSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientValidationList = _reflection.GeneratedProtocolMessageType('ClientValidationList', (_message.Message,), {

  'ClientsEntry' : _reflection.GeneratedProtocolMessageType('ClientsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CLIENTVALIDATIONLIST_CLIENTSENTRY,
    '__module__' : 'other_models_pb2'
    # @@protoc_insertion_point(class_scope:ClientValidationList.ClientsEntry)
    })
  ,
  'DESCRIPTOR' : _CLIENTVALIDATIONLIST,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:ClientValidationList)
  })
_sym_db.RegisterMessage(ClientValidationList)
_sym_db.RegisterMessage(ClientValidationList.ClientsEntry)

Payment = _reflection.GeneratedProtocolMessageType('Payment', (_message.Message,), {
  'DESCRIPTOR' : _PAYMENT,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:Payment)
  })
_sym_db.RegisterMessage(Payment)

CompletedPayment = _reflection.GeneratedProtocolMessageType('CompletedPayment', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETEDPAYMENT,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:CompletedPayment)
  })
_sym_db.RegisterMessage(CompletedPayment)

RecentPaymentsRequest = _reflection.GeneratedProtocolMessageType('RecentPaymentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECENTPAYMENTSREQUEST,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:RecentPaymentsRequest)
  })
_sym_db.RegisterMessage(RecentPaymentsRequest)

RecentPaymentsResponce = _reflection.GeneratedProtocolMessageType('RecentPaymentsResponce', (_message.Message,), {
  'DESCRIPTOR' : _RECENTPAYMENTSRESPONCE,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:RecentPaymentsResponce)
  })
_sym_db.RegisterMessage(RecentPaymentsResponce)

UserInfoRequest = _reflection.GeneratedProtocolMessageType('UserInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERINFOREQUEST,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:UserInfoRequest)
  })
_sym_db.RegisterMessage(UserInfoRequest)

UserInfoResponse = _reflection.GeneratedProtocolMessageType('UserInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERINFORESPONSE,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:UserInfoResponse)
  })
_sym_db.RegisterMessage(UserInfoResponse)

SessionOpenRequest = _reflection.GeneratedProtocolMessageType('SessionOpenRequest', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONOPENREQUEST,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:SessionOpenRequest)
  })
_sym_db.RegisterMessage(SessionOpenRequest)

SessionOpenResponce = _reflection.GeneratedProtocolMessageType('SessionOpenResponce', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONOPENRESPONCE,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:SessionOpenResponce)
  })
_sym_db.RegisterMessage(SessionOpenResponce)

SessionCloseRequest = _reflection.GeneratedProtocolMessageType('SessionCloseRequest', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONCLOSEREQUEST,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:SessionCloseRequest)
  })
_sym_db.RegisterMessage(SessionCloseRequest)

GetPriceRequest = _reflection.GeneratedProtocolMessageType('GetPriceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPRICEREQUEST,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:GetPriceRequest)
  })
_sym_db.RegisterMessage(GetPriceRequest)

GetPriceResponse = _reflection.GeneratedProtocolMessageType('GetPriceResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPRICERESPONSE,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:GetPriceResponse)
  })
_sym_db.RegisterMessage(GetPriceResponse)

TransactionSyncRequest = _reflection.GeneratedProtocolMessageType('TransactionSyncRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONSYNCREQUEST,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:TransactionSyncRequest)
  })
_sym_db.RegisterMessage(TransactionSyncRequest)

RefilRequest = _reflection.GeneratedProtocolMessageType('RefilRequest', (_message.Message,), {
  'DESCRIPTOR' : _REFILREQUEST,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:RefilRequest)
  })
_sym_db.RegisterMessage(RefilRequest)

TrafficStatPoint = _reflection.GeneratedProtocolMessageType('TrafficStatPoint', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICSTATPOINT,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:TrafficStatPoint)
  })
_sym_db.RegisterMessage(TrafficStatPoint)

TrafficStatsResponce = _reflection.GeneratedProtocolMessageType('TrafficStatsResponce', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICSTATSRESPONCE,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:TrafficStatsResponce)
  })
_sym_db.RegisterMessage(TrafficStatsResponce)

TrafficStatsRequest = _reflection.GeneratedProtocolMessageType('TrafficStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICSTATSREQUEST,
  '__module__' : 'other_models_pb2'
  # @@protoc_insertion_point(class_scope:TrafficStatsRequest)
  })
_sym_db.RegisterMessage(TrafficStatsRequest)


_CLIENTVALIDATIONLIST_CLIENTSENTRY._options = None
# @@protoc_insertion_point(module_scope)
