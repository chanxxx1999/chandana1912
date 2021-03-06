# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: form_inputs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='form_inputs.proto',
  package='Application',
  syntax='proto3',
  serialized_options=_b('Z>cd.splunkdev.com/mobile/spacebridge-golang-protos/splunkcx/ssg'),
  serialized_pb=_b('\n\x11\x66orm_inputs.proto\x12\x0b\x41pplication\"K\n\nTimepicker\x12\r\n\x05label\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65\x66\x61ultEarliest\x18\x02 \x01(\t\x12\x15\n\rdefaultLatest\x18\x03 \x01(\t\"\xa0\x03\n\x08\x44ropdown\x12\r\n\x05label\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x65\x66\x61ultValue\x18\x02 \x01(\t\x12\x14\n\x0cinitialValue\x18\x03 \x01(\t\x12\x41\n\x0e\x63hoiceValueMap\x18\x04 \x03(\x0b\x32).Application.Dropdown.ChoiceValueMapEntry\x12\x13\n\x0btokenPrefix\x18\x05 \x01(\t\x12\x13\n\x0btokenSuffix\x18\x06 \x01(\t\x12\x31\n\x0f\x63hoiceValueList\x18\x07 \x03(\x0b\x32\x18.Application.ChoiceValue\x12\x33\n\x0e\x64ynamicOptions\x18\x08 \x01(\x0b\x32\x1b.Application.DynamicOptions\x12\x19\n\x11selectFirstChoice\x18\t \x01(\x08\x12\x17\n\x0fshowClearButton\x18\n \x01(\x08\x12\x19\n\x11\x61llowCustomValues\x18\x0b \x01(\x08\x1a\x35\n\x13\x43hoiceValueMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe6\x02\n\x05Radio\x12\r\n\x05label\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x65\x66\x61ultValue\x18\x02 \x01(\t\x12\x14\n\x0cinitialValue\x18\x03 \x01(\t\x12>\n\x0e\x63hoiceValueMap\x18\x04 \x03(\x0b\x32&.Application.Radio.ChoiceValueMapEntry\x12\x13\n\x0btokenPrefix\x18\x05 \x01(\t\x12\x13\n\x0btokenSuffix\x18\x06 \x01(\t\x12\x31\n\x0f\x63hoiceValueList\x18\x07 \x03(\x0b\x32\x18.Application.ChoiceValue\x12\x33\n\x0e\x64ynamicOptions\x18\x08 \x01(\x0b\x32\x1b.Application.DynamicOptions\x12\x19\n\x11selectFirstChoice\x18\t \x01(\x08\x1a\x35\n\x13\x43hoiceValueMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x98\x03\n\x08\x43heckbox\x12\r\n\x05label\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x65\x66\x61ultValue\x18\x02 \x01(\t\x12\x14\n\x0cinitialValue\x18\x03 \x01(\t\x12\x41\n\x0e\x63hoiceValueMap\x18\x04 \x03(\x0b\x32).Application.Checkbox.ChoiceValueMapEntry\x12\x13\n\x0btokenPrefix\x18\x05 \x01(\t\x12\x13\n\x0btokenSuffix\x18\x06 \x01(\t\x12\x18\n\x10tokenValuePrefix\x18\x07 \x01(\t\x12\x18\n\x10tokenValueSuffix\x18\x08 \x01(\t\x12\x11\n\tdelimiter\x18\t \x01(\t\x12\x31\n\x0f\x63hoiceValueList\x18\n \x03(\x0b\x32\x18.Application.ChoiceValue\x12\x33\n\x0e\x64ynamicOptions\x18\x0b \x01(\x0b\x32\x1b.Application.DynamicOptions\x1a\x35\n\x13\x43hoiceValueMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"n\n\x07Textbox\x12\r\n\x05label\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x65\x66\x61ultValue\x18\x02 \x01(\t\x12\x14\n\x0cinitialValue\x18\x03 \x01(\t\x12\x13\n\x0btokenPrefix\x18\x05 \x01(\t\x12\x13\n\x0btokenSuffix\x18\x06 \x01(\t\"\xb9\x03\n\x0bMultiselect\x12\r\n\x05label\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x65\x66\x61ultValue\x18\x02 \x01(\t\x12\x14\n\x0cinitialValue\x18\x03 \x01(\t\x12\x44\n\x0e\x63hoiceValueMap\x18\x04 \x03(\x0b\x32,.Application.Multiselect.ChoiceValueMapEntry\x12\x13\n\x0btokenPrefix\x18\x05 \x01(\t\x12\x13\n\x0btokenSuffix\x18\x06 \x01(\t\x12\x18\n\x10tokenValuePrefix\x18\x07 \x01(\t\x12\x18\n\x10tokenValueSuffix\x18\x08 \x01(\t\x12\x11\n\tdelimiter\x18\t \x01(\t\x12\x31\n\x0f\x63hoiceValueList\x18\n \x03(\x0b\x32\x18.Application.ChoiceValue\x12\x33\n\x0e\x64ynamicOptions\x18\x0b \x01(\x0b\x32\x1b.Application.DynamicOptions\x12\x19\n\x11\x61llowCustomValues\x18\x0c \x01(\x08\x1a\x35\n\x13\x43hoiceValueMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\",\n\x0b\x43hoiceValue\x12\x0e\n\x06\x63hoice\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"i\n\x0e\x44ynamicOptions\x12\x15\n\rfieldForLabel\x18\x01 \x01(\t\x12\x15\n\rfieldForValue\x18\x02 \x01(\t\x12\x0f\n\x07queryId\x18\x03 \x01(\t\x12\x18\n\x10searchTokenNames\x18\x04 \x03(\tB@Z>cd.splunkdev.com/mobile/spacebridge-golang-protos/splunkcx/ssgb\x06proto3')
)




_TIMEPICKER = _descriptor.Descriptor(
  name='Timepicker',
  full_name='Application.Timepicker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='Application.Timepicker.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultEarliest', full_name='Application.Timepicker.defaultEarliest', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultLatest', full_name='Application.Timepicker.defaultLatest', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=34,
  serialized_end=109,
)


_DROPDOWN_CHOICEVALUEMAPENTRY = _descriptor.Descriptor(
  name='ChoiceValueMapEntry',
  full_name='Application.Dropdown.ChoiceValueMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Application.Dropdown.ChoiceValueMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Application.Dropdown.ChoiceValueMapEntry.value', index=1,
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
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=475,
  serialized_end=528,
)

_DROPDOWN = _descriptor.Descriptor(
  name='Dropdown',
  full_name='Application.Dropdown',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='Application.Dropdown.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultValue', full_name='Application.Dropdown.defaultValue', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initialValue', full_name='Application.Dropdown.initialValue', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='choiceValueMap', full_name='Application.Dropdown.choiceValueMap', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenPrefix', full_name='Application.Dropdown.tokenPrefix', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenSuffix', full_name='Application.Dropdown.tokenSuffix', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='choiceValueList', full_name='Application.Dropdown.choiceValueList', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dynamicOptions', full_name='Application.Dropdown.dynamicOptions', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selectFirstChoice', full_name='Application.Dropdown.selectFirstChoice', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='showClearButton', full_name='Application.Dropdown.showClearButton', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allowCustomValues', full_name='Application.Dropdown.allowCustomValues', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DROPDOWN_CHOICEVALUEMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=528,
)


_RADIO_CHOICEVALUEMAPENTRY = _descriptor.Descriptor(
  name='ChoiceValueMapEntry',
  full_name='Application.Radio.ChoiceValueMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Application.Radio.ChoiceValueMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Application.Radio.ChoiceValueMapEntry.value', index=1,
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
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=475,
  serialized_end=528,
)

_RADIO = _descriptor.Descriptor(
  name='Radio',
  full_name='Application.Radio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='Application.Radio.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultValue', full_name='Application.Radio.defaultValue', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initialValue', full_name='Application.Radio.initialValue', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='choiceValueMap', full_name='Application.Radio.choiceValueMap', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenPrefix', full_name='Application.Radio.tokenPrefix', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenSuffix', full_name='Application.Radio.tokenSuffix', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='choiceValueList', full_name='Application.Radio.choiceValueList', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dynamicOptions', full_name='Application.Radio.dynamicOptions', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selectFirstChoice', full_name='Application.Radio.selectFirstChoice', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RADIO_CHOICEVALUEMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=531,
  serialized_end=889,
)


_CHECKBOX_CHOICEVALUEMAPENTRY = _descriptor.Descriptor(
  name='ChoiceValueMapEntry',
  full_name='Application.Checkbox.ChoiceValueMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Application.Checkbox.ChoiceValueMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Application.Checkbox.ChoiceValueMapEntry.value', index=1,
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
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=475,
  serialized_end=528,
)

_CHECKBOX = _descriptor.Descriptor(
  name='Checkbox',
  full_name='Application.Checkbox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='Application.Checkbox.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultValue', full_name='Application.Checkbox.defaultValue', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initialValue', full_name='Application.Checkbox.initialValue', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='choiceValueMap', full_name='Application.Checkbox.choiceValueMap', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenPrefix', full_name='Application.Checkbox.tokenPrefix', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenSuffix', full_name='Application.Checkbox.tokenSuffix', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenValuePrefix', full_name='Application.Checkbox.tokenValuePrefix', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenValueSuffix', full_name='Application.Checkbox.tokenValueSuffix', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delimiter', full_name='Application.Checkbox.delimiter', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='choiceValueList', full_name='Application.Checkbox.choiceValueList', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dynamicOptions', full_name='Application.Checkbox.dynamicOptions', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHECKBOX_CHOICEVALUEMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=892,
  serialized_end=1300,
)


_TEXTBOX = _descriptor.Descriptor(
  name='Textbox',
  full_name='Application.Textbox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='Application.Textbox.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultValue', full_name='Application.Textbox.defaultValue', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initialValue', full_name='Application.Textbox.initialValue', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenPrefix', full_name='Application.Textbox.tokenPrefix', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenSuffix', full_name='Application.Textbox.tokenSuffix', index=4,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=1302,
  serialized_end=1412,
)


_MULTISELECT_CHOICEVALUEMAPENTRY = _descriptor.Descriptor(
  name='ChoiceValueMapEntry',
  full_name='Application.Multiselect.ChoiceValueMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Application.Multiselect.ChoiceValueMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Application.Multiselect.ChoiceValueMapEntry.value', index=1,
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
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=475,
  serialized_end=528,
)

_MULTISELECT = _descriptor.Descriptor(
  name='Multiselect',
  full_name='Application.Multiselect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='Application.Multiselect.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultValue', full_name='Application.Multiselect.defaultValue', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initialValue', full_name='Application.Multiselect.initialValue', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='choiceValueMap', full_name='Application.Multiselect.choiceValueMap', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenPrefix', full_name='Application.Multiselect.tokenPrefix', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenSuffix', full_name='Application.Multiselect.tokenSuffix', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenValuePrefix', full_name='Application.Multiselect.tokenValuePrefix', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenValueSuffix', full_name='Application.Multiselect.tokenValueSuffix', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delimiter', full_name='Application.Multiselect.delimiter', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='choiceValueList', full_name='Application.Multiselect.choiceValueList', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dynamicOptions', full_name='Application.Multiselect.dynamicOptions', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allowCustomValues', full_name='Application.Multiselect.allowCustomValues', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MULTISELECT_CHOICEVALUEMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1415,
  serialized_end=1856,
)


_CHOICEVALUE = _descriptor.Descriptor(
  name='ChoiceValue',
  full_name='Application.ChoiceValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='choice', full_name='Application.ChoiceValue.choice', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Application.ChoiceValue.value', index=1,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1858,
  serialized_end=1902,
)


_DYNAMICOPTIONS = _descriptor.Descriptor(
  name='DynamicOptions',
  full_name='Application.DynamicOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fieldForLabel', full_name='Application.DynamicOptions.fieldForLabel', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fieldForValue', full_name='Application.DynamicOptions.fieldForValue', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queryId', full_name='Application.DynamicOptions.queryId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='searchTokenNames', full_name='Application.DynamicOptions.searchTokenNames', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=1904,
  serialized_end=2009,
)

_DROPDOWN_CHOICEVALUEMAPENTRY.containing_type = _DROPDOWN
_DROPDOWN.fields_by_name['choiceValueMap'].message_type = _DROPDOWN_CHOICEVALUEMAPENTRY
_DROPDOWN.fields_by_name['choiceValueList'].message_type = _CHOICEVALUE
_DROPDOWN.fields_by_name['dynamicOptions'].message_type = _DYNAMICOPTIONS
_RADIO_CHOICEVALUEMAPENTRY.containing_type = _RADIO
_RADIO.fields_by_name['choiceValueMap'].message_type = _RADIO_CHOICEVALUEMAPENTRY
_RADIO.fields_by_name['choiceValueList'].message_type = _CHOICEVALUE
_RADIO.fields_by_name['dynamicOptions'].message_type = _DYNAMICOPTIONS
_CHECKBOX_CHOICEVALUEMAPENTRY.containing_type = _CHECKBOX
_CHECKBOX.fields_by_name['choiceValueMap'].message_type = _CHECKBOX_CHOICEVALUEMAPENTRY
_CHECKBOX.fields_by_name['choiceValueList'].message_type = _CHOICEVALUE
_CHECKBOX.fields_by_name['dynamicOptions'].message_type = _DYNAMICOPTIONS
_MULTISELECT_CHOICEVALUEMAPENTRY.containing_type = _MULTISELECT
_MULTISELECT.fields_by_name['choiceValueMap'].message_type = _MULTISELECT_CHOICEVALUEMAPENTRY
_MULTISELECT.fields_by_name['choiceValueList'].message_type = _CHOICEVALUE
_MULTISELECT.fields_by_name['dynamicOptions'].message_type = _DYNAMICOPTIONS
DESCRIPTOR.message_types_by_name['Timepicker'] = _TIMEPICKER
DESCRIPTOR.message_types_by_name['Dropdown'] = _DROPDOWN
DESCRIPTOR.message_types_by_name['Radio'] = _RADIO
DESCRIPTOR.message_types_by_name['Checkbox'] = _CHECKBOX
DESCRIPTOR.message_types_by_name['Textbox'] = _TEXTBOX
DESCRIPTOR.message_types_by_name['Multiselect'] = _MULTISELECT
DESCRIPTOR.message_types_by_name['ChoiceValue'] = _CHOICEVALUE
DESCRIPTOR.message_types_by_name['DynamicOptions'] = _DYNAMICOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Timepicker = _reflection.GeneratedProtocolMessageType('Timepicker', (_message.Message,), dict(
  DESCRIPTOR = _TIMEPICKER,
  __module__ = 'form_inputs_pb2'
  # @@protoc_insertion_point(class_scope:Application.Timepicker)
  ))
_sym_db.RegisterMessage(Timepicker)

Dropdown = _reflection.GeneratedProtocolMessageType('Dropdown', (_message.Message,), dict(

  ChoiceValueMapEntry = _reflection.GeneratedProtocolMessageType('ChoiceValueMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _DROPDOWN_CHOICEVALUEMAPENTRY,
    __module__ = 'form_inputs_pb2'
    # @@protoc_insertion_point(class_scope:Application.Dropdown.ChoiceValueMapEntry)
    ))
  ,
  DESCRIPTOR = _DROPDOWN,
  __module__ = 'form_inputs_pb2'
  # @@protoc_insertion_point(class_scope:Application.Dropdown)
  ))
_sym_db.RegisterMessage(Dropdown)
_sym_db.RegisterMessage(Dropdown.ChoiceValueMapEntry)

Radio = _reflection.GeneratedProtocolMessageType('Radio', (_message.Message,), dict(

  ChoiceValueMapEntry = _reflection.GeneratedProtocolMessageType('ChoiceValueMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _RADIO_CHOICEVALUEMAPENTRY,
    __module__ = 'form_inputs_pb2'
    # @@protoc_insertion_point(class_scope:Application.Radio.ChoiceValueMapEntry)
    ))
  ,
  DESCRIPTOR = _RADIO,
  __module__ = 'form_inputs_pb2'
  # @@protoc_insertion_point(class_scope:Application.Radio)
  ))
_sym_db.RegisterMessage(Radio)
_sym_db.RegisterMessage(Radio.ChoiceValueMapEntry)

Checkbox = _reflection.GeneratedProtocolMessageType('Checkbox', (_message.Message,), dict(

  ChoiceValueMapEntry = _reflection.GeneratedProtocolMessageType('ChoiceValueMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _CHECKBOX_CHOICEVALUEMAPENTRY,
    __module__ = 'form_inputs_pb2'
    # @@protoc_insertion_point(class_scope:Application.Checkbox.ChoiceValueMapEntry)
    ))
  ,
  DESCRIPTOR = _CHECKBOX,
  __module__ = 'form_inputs_pb2'
  # @@protoc_insertion_point(class_scope:Application.Checkbox)
  ))
_sym_db.RegisterMessage(Checkbox)
_sym_db.RegisterMessage(Checkbox.ChoiceValueMapEntry)

Textbox = _reflection.GeneratedProtocolMessageType('Textbox', (_message.Message,), dict(
  DESCRIPTOR = _TEXTBOX,
  __module__ = 'form_inputs_pb2'
  # @@protoc_insertion_point(class_scope:Application.Textbox)
  ))
_sym_db.RegisterMessage(Textbox)

Multiselect = _reflection.GeneratedProtocolMessageType('Multiselect', (_message.Message,), dict(

  ChoiceValueMapEntry = _reflection.GeneratedProtocolMessageType('ChoiceValueMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _MULTISELECT_CHOICEVALUEMAPENTRY,
    __module__ = 'form_inputs_pb2'
    # @@protoc_insertion_point(class_scope:Application.Multiselect.ChoiceValueMapEntry)
    ))
  ,
  DESCRIPTOR = _MULTISELECT,
  __module__ = 'form_inputs_pb2'
  # @@protoc_insertion_point(class_scope:Application.Multiselect)
  ))
_sym_db.RegisterMessage(Multiselect)
_sym_db.RegisterMessage(Multiselect.ChoiceValueMapEntry)

ChoiceValue = _reflection.GeneratedProtocolMessageType('ChoiceValue', (_message.Message,), dict(
  DESCRIPTOR = _CHOICEVALUE,
  __module__ = 'form_inputs_pb2'
  # @@protoc_insertion_point(class_scope:Application.ChoiceValue)
  ))
_sym_db.RegisterMessage(ChoiceValue)

DynamicOptions = _reflection.GeneratedProtocolMessageType('DynamicOptions', (_message.Message,), dict(
  DESCRIPTOR = _DYNAMICOPTIONS,
  __module__ = 'form_inputs_pb2'
  # @@protoc_insertion_point(class_scope:Application.DynamicOptions)
  ))
_sym_db.RegisterMessage(DynamicOptions)


DESCRIPTOR._options = None
_DROPDOWN_CHOICEVALUEMAPENTRY._options = None
_RADIO_CHOICEVALUEMAPENTRY._options = None
_CHECKBOX_CHOICEVALUEMAPENTRY._options = None
_MULTISELECT_CHOICEVALUEMAPENTRY._options = None
# @@protoc_insertion_point(module_scope)
