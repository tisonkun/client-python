# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: engula/v1/database.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x65ngula/v1/database.proto\x12\tengula.v1\"}\n\x0f\x44\x61tabaseRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x07selects\x18\x02 \x03(\x0b\x32\x1c.engula.v1.CollectionRequest\x12-\n\x07mutates\x18\x03 \x03(\x0b\x32\x1c.engula.v1.CollectionRequest\"r\n\x10\x44\x61tabaseResponse\x12.\n\x07selects\x18\x01 \x03(\x0b\x32\x1d.engula.v1.CollectionResponse\x12.\n\x07mutates\x18\x02 \x03(\x0b\x32\x1d.engula.v1.CollectionResponse\"S\n\x11\x43ollectionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03ids\x18\x02 \x03(\x0c\x12#\n\x05\x65xprs\x18\x03 \x03(\x0b\x32\x14.engula.v1.TypedExpr\";\n\x12\x43ollectionResponse\x12%\n\x06values\x18\x01 \x03(\x0b\x32\x15.engula.v1.TypedValue\",\n\x07I64Expr\x12!\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x13.engula.v1.CallExpr\",\n\x07\x46\x36\x34\x45xpr\x12!\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x13.engula.v1.CallExpr\"-\n\x08\x42lobExpr\x12!\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x13.engula.v1.CallExpr\"-\n\x08TextExpr\x12!\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x13.engula.v1.CallExpr\"-\n\x08ListExpr\x12!\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x13.engula.v1.CallExpr\",\n\x07MapExpr\x12!\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x13.engula.v1.CallExpr\",\n\x07SetExpr\x12!\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x13.engula.v1.CallExpr\",\n\x07\x41nyExpr\x12!\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x13.engula.v1.CallExpr\"R\n\x08\x43\x61llExpr\x12!\n\x04\x66unc\x18\x01 \x01(\x0e\x32\x13.engula.v1.Function\x12#\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x15.engula.v1.TypedValue\"\xd9\x02\n\tTypedExpr\x12&\n\x08i64_expr\x18\x01 \x01(\x0b\x32\x12.engula.v1.I64ExprH\x00\x12&\n\x08\x66\x36\x34_expr\x18\x02 \x01(\x0b\x32\x12.engula.v1.F64ExprH\x00\x12(\n\tblob_expr\x18\x03 \x01(\x0b\x32\x13.engula.v1.BlobExprH\x00\x12(\n\ttext_expr\x18\x04 \x01(\x0b\x32\x13.engula.v1.TextExprH\x00\x12(\n\tlist_expr\x18\x05 \x01(\x0b\x32\x13.engula.v1.ListExprH\x00\x12&\n\x08map_expr\x18\x06 \x01(\x0b\x32\x12.engula.v1.MapExprH\x00\x12&\n\x08set_expr\x18\x07 \x01(\x0b\x32\x12.engula.v1.SetExprH\x00\x12&\n\x08\x61ny_expr\x18\x0f \x01(\x0b\x32\x12.engula.v1.AnyExprH\x00\x42\x06\n\x04\x65xpr\"\x99\x02\n\nTypedValue\x12\x13\n\ti64_value\x18\x01 \x01(\x12H\x00\x12\x13\n\tf64_value\x18\x02 \x01(\x01H\x00\x12\x14\n\nblob_value\x18\x03 \x01(\x0cH\x00\x12\x14\n\ntext_value\x18\x04 \x01(\tH\x00\x12*\n\nlist_value\x18\x05 \x01(\x0b\x32\x14.engula.v1.ListValueH\x00\x12(\n\tmap_value\x18\x06 \x01(\x0b\x32\x13.engula.v1.MapValueH\x00\x12(\n\tset_value\x18\x07 \x01(\x0b\x32\x13.engula.v1.SetValueH\x00\x12,\n\x0brange_value\x18\x0f \x01(\x0b\x32\x15.engula.v1.RangeValueH\x00\x42\x07\n\x05value\"T\n\x08MapValue\x12\"\n\x04keys\x18\x01 \x01(\x0b\x32\x14.engula.v1.ListValue\x12$\n\x06values\x18\x02 \x01(\x0b\x32\x14.engula.v1.ListValue\".\n\x08SetValue\x12\"\n\x04keys\x18\x01 \x01(\x0b\x32\x14.engula.v1.ListValue\"Y\n\tListValue\x12\x11\n\ti64_value\x18\x01 \x03(\x12\x12\x11\n\tf64_value\x18\x02 \x03(\x01\x12\x12\n\nblob_value\x18\x03 \x03(\x0c\x12\x12\n\ntext_value\x18\x04 \x03(\t\"}\n\nRangeBound\x12\x13\n\ti64_value\x18\x01 \x01(\x12H\x00\x12\x13\n\tf64_value\x18\x02 \x01(\x01H\x00\x12\x14\n\nblob_value\x18\x03 \x01(\x0cH\x00\x12\x14\n\ntext_value\x18\x04 \x01(\tH\x00\x12\x10\n\x08included\x18\x0f \x01(\x08\x42\x07\n\x05value\"V\n\nRangeValue\x12$\n\x05start\x18\x01 \x01(\x0b\x32\x15.engula.v1.RangeBound\x12\"\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x15.engula.v1.RangeBound*\xca\x01\n\x08\x46unction\x12\x07\n\x03GET\x10\x00\x12\x07\n\x03SET\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x12\n\n\x06\x45XISTS\x10\x03\x12\x07\n\x03\x41\x44\x44\x10\n\x12\x07\n\x03SUB\x10\x0b\x12\x08\n\x04TRIM\x10\x1e\x12\x08\n\x04LPOP\x10\x1f\x12\x08\n\x04RPOP\x10 \x12\t\n\x05LPUSH\x10!\x12\t\n\x05RPUSH\x10\"\x12\x07\n\x03LEN\x10(\x12\t\n\x05INDEX\x10)\x12\t\n\x05RANGE\x10*\x12\t\n\x05\x43LEAR\x10+\x12\n\n\x06\x45XTEND\x10,\x12\n\n\x06REMOVE\x10-\x12\x0c\n\x08\x43ONTAINS\x10.b\x06proto3')

_FUNCTION = DESCRIPTOR.enum_types_by_name['Function']
Function = enum_type_wrapper.EnumTypeWrapper(_FUNCTION)
GET = 0
SET = 1
DELETE = 2
EXISTS = 3
ADD = 10
SUB = 11
TRIM = 30
LPOP = 31
RPOP = 32
LPUSH = 33
RPUSH = 34
LEN = 40
INDEX = 41
RANGE = 42
CLEAR = 43
EXTEND = 44
REMOVE = 45
CONTAINS = 46


_DATABASEREQUEST = DESCRIPTOR.message_types_by_name['DatabaseRequest']
_DATABASERESPONSE = DESCRIPTOR.message_types_by_name['DatabaseResponse']
_COLLECTIONREQUEST = DESCRIPTOR.message_types_by_name['CollectionRequest']
_COLLECTIONRESPONSE = DESCRIPTOR.message_types_by_name['CollectionResponse']
_I64EXPR = DESCRIPTOR.message_types_by_name['I64Expr']
_F64EXPR = DESCRIPTOR.message_types_by_name['F64Expr']
_BLOBEXPR = DESCRIPTOR.message_types_by_name['BlobExpr']
_TEXTEXPR = DESCRIPTOR.message_types_by_name['TextExpr']
_LISTEXPR = DESCRIPTOR.message_types_by_name['ListExpr']
_MAPEXPR = DESCRIPTOR.message_types_by_name['MapExpr']
_SETEXPR = DESCRIPTOR.message_types_by_name['SetExpr']
_ANYEXPR = DESCRIPTOR.message_types_by_name['AnyExpr']
_CALLEXPR = DESCRIPTOR.message_types_by_name['CallExpr']
_TYPEDEXPR = DESCRIPTOR.message_types_by_name['TypedExpr']
_TYPEDVALUE = DESCRIPTOR.message_types_by_name['TypedValue']
_MAPVALUE = DESCRIPTOR.message_types_by_name['MapValue']
_SETVALUE = DESCRIPTOR.message_types_by_name['SetValue']
_LISTVALUE = DESCRIPTOR.message_types_by_name['ListValue']
_RANGEBOUND = DESCRIPTOR.message_types_by_name['RangeBound']
_RANGEVALUE = DESCRIPTOR.message_types_by_name['RangeValue']
DatabaseRequest = _reflection.GeneratedProtocolMessageType('DatabaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _DATABASEREQUEST,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.DatabaseRequest)
  })
_sym_db.RegisterMessage(DatabaseRequest)

DatabaseResponse = _reflection.GeneratedProtocolMessageType('DatabaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _DATABASERESPONSE,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.DatabaseResponse)
  })
_sym_db.RegisterMessage(DatabaseResponse)

CollectionRequest = _reflection.GeneratedProtocolMessageType('CollectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONREQUEST,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.CollectionRequest)
  })
_sym_db.RegisterMessage(CollectionRequest)

CollectionResponse = _reflection.GeneratedProtocolMessageType('CollectionResponse', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONRESPONSE,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.CollectionResponse)
  })
_sym_db.RegisterMessage(CollectionResponse)

I64Expr = _reflection.GeneratedProtocolMessageType('I64Expr', (_message.Message,), {
  'DESCRIPTOR' : _I64EXPR,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.I64Expr)
  })
_sym_db.RegisterMessage(I64Expr)

F64Expr = _reflection.GeneratedProtocolMessageType('F64Expr', (_message.Message,), {
  'DESCRIPTOR' : _F64EXPR,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.F64Expr)
  })
_sym_db.RegisterMessage(F64Expr)

BlobExpr = _reflection.GeneratedProtocolMessageType('BlobExpr', (_message.Message,), {
  'DESCRIPTOR' : _BLOBEXPR,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.BlobExpr)
  })
_sym_db.RegisterMessage(BlobExpr)

TextExpr = _reflection.GeneratedProtocolMessageType('TextExpr', (_message.Message,), {
  'DESCRIPTOR' : _TEXTEXPR,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.TextExpr)
  })
_sym_db.RegisterMessage(TextExpr)

ListExpr = _reflection.GeneratedProtocolMessageType('ListExpr', (_message.Message,), {
  'DESCRIPTOR' : _LISTEXPR,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.ListExpr)
  })
_sym_db.RegisterMessage(ListExpr)

MapExpr = _reflection.GeneratedProtocolMessageType('MapExpr', (_message.Message,), {
  'DESCRIPTOR' : _MAPEXPR,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.MapExpr)
  })
_sym_db.RegisterMessage(MapExpr)

SetExpr = _reflection.GeneratedProtocolMessageType('SetExpr', (_message.Message,), {
  'DESCRIPTOR' : _SETEXPR,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.SetExpr)
  })
_sym_db.RegisterMessage(SetExpr)

AnyExpr = _reflection.GeneratedProtocolMessageType('AnyExpr', (_message.Message,), {
  'DESCRIPTOR' : _ANYEXPR,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.AnyExpr)
  })
_sym_db.RegisterMessage(AnyExpr)

CallExpr = _reflection.GeneratedProtocolMessageType('CallExpr', (_message.Message,), {
  'DESCRIPTOR' : _CALLEXPR,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.CallExpr)
  })
_sym_db.RegisterMessage(CallExpr)

TypedExpr = _reflection.GeneratedProtocolMessageType('TypedExpr', (_message.Message,), {
  'DESCRIPTOR' : _TYPEDEXPR,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.TypedExpr)
  })
_sym_db.RegisterMessage(TypedExpr)

TypedValue = _reflection.GeneratedProtocolMessageType('TypedValue', (_message.Message,), {
  'DESCRIPTOR' : _TYPEDVALUE,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.TypedValue)
  })
_sym_db.RegisterMessage(TypedValue)

MapValue = _reflection.GeneratedProtocolMessageType('MapValue', (_message.Message,), {
  'DESCRIPTOR' : _MAPVALUE,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.MapValue)
  })
_sym_db.RegisterMessage(MapValue)

SetValue = _reflection.GeneratedProtocolMessageType('SetValue', (_message.Message,), {
  'DESCRIPTOR' : _SETVALUE,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.SetValue)
  })
_sym_db.RegisterMessage(SetValue)

ListValue = _reflection.GeneratedProtocolMessageType('ListValue', (_message.Message,), {
  'DESCRIPTOR' : _LISTVALUE,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.ListValue)
  })
_sym_db.RegisterMessage(ListValue)

RangeBound = _reflection.GeneratedProtocolMessageType('RangeBound', (_message.Message,), {
  'DESCRIPTOR' : _RANGEBOUND,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.RangeBound)
  })
_sym_db.RegisterMessage(RangeBound)

RangeValue = _reflection.GeneratedProtocolMessageType('RangeValue', (_message.Message,), {
  'DESCRIPTOR' : _RANGEVALUE,
  '__module__' : 'engula.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.RangeValue)
  })
_sym_db.RegisterMessage(RangeValue)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FUNCTION._serialized_start=1956
  _FUNCTION._serialized_end=2158
  _DATABASEREQUEST._serialized_start=39
  _DATABASEREQUEST._serialized_end=164
  _DATABASERESPONSE._serialized_start=166
  _DATABASERESPONSE._serialized_end=280
  _COLLECTIONREQUEST._serialized_start=282
  _COLLECTIONREQUEST._serialized_end=365
  _COLLECTIONRESPONSE._serialized_start=367
  _COLLECTIONRESPONSE._serialized_end=426
  _I64EXPR._serialized_start=428
  _I64EXPR._serialized_end=472
  _F64EXPR._serialized_start=474
  _F64EXPR._serialized_end=518
  _BLOBEXPR._serialized_start=520
  _BLOBEXPR._serialized_end=565
  _TEXTEXPR._serialized_start=567
  _TEXTEXPR._serialized_end=612
  _LISTEXPR._serialized_start=614
  _LISTEXPR._serialized_end=659
  _MAPEXPR._serialized_start=661
  _MAPEXPR._serialized_end=705
  _SETEXPR._serialized_start=707
  _SETEXPR._serialized_end=751
  _ANYEXPR._serialized_start=753
  _ANYEXPR._serialized_end=797
  _CALLEXPR._serialized_start=799
  _CALLEXPR._serialized_end=881
  _TYPEDEXPR._serialized_start=884
  _TYPEDEXPR._serialized_end=1229
  _TYPEDVALUE._serialized_start=1232
  _TYPEDVALUE._serialized_end=1513
  _MAPVALUE._serialized_start=1515
  _MAPVALUE._serialized_end=1599
  _SETVALUE._serialized_start=1601
  _SETVALUE._serialized_end=1647
  _LISTVALUE._serialized_start=1649
  _LISTVALUE._serialized_end=1738
  _RANGEBOUND._serialized_start=1740
  _RANGEBOUND._serialized_end=1865
  _RANGEVALUE._serialized_start=1867
  _RANGEVALUE._serialized_end=1953
# @@protoc_insertion_point(module_scope)
