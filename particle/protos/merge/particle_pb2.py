# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: merge/particle.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14merge/particle.proto\x12\x1a\x63om.yunlong.particle.proto\"j\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x37\n\x06phones\x18\x04 \x03(\x0b\x32\'.com.yunlong.particle.proto.PhoneNumber\"R\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x01(\t\x12\x33\n\x04type\x18\x02 \x01(\x0e\x32%.com.yunlong.particle.proto.PhoneType\"A\n\x0b\x41\x64\x64ressBook\x12\x32\n\x06people\x18\x01 \x03(\x0b\x32\".com.yunlong.particle.proto.Person*+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'merge.particle_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PHONETYPE._serialized_start=311
  _PHONETYPE._serialized_end=354
  _PERSON._serialized_start=52
  _PERSON._serialized_end=158
  _PHONENUMBER._serialized_start=160
  _PHONENUMBER._serialized_end=242
  _ADDRESSBOOK._serialized_start=244
  _ADDRESSBOOK._serialized_end=309
# @@protoc_insertion_point(module_scope)
