# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dota_commonmessages.proto
# Protobuf Python Version: 6.30.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    0,
    '',
    'dota_commonmessages.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import networkbasetypes_pb2 as networkbasetypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x64ota_commonmessages.proto\x1a\x16networkbasetypes.proto\"\xaa\x01\n\x15\x43\x44OTAMsg_LocationPing\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\x12\n\x06target\x18\x03 \x01(\x05:\x02-1\x12\x13\n\x0b\x64irect_ping\x18\x04 \x01(\x08\x12\x18\n\x04type\x18\x05 \x01(\r:\n4294967295\x12\x38\n\x0bping_source\x18\x06 \x01(\x0e\x32\x0c.EPingSource:\x15k_ePingSource_Default\"G\n\x12\x43\x44OTAMsg_ItemAlert\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\x1b\n\x0fitem_ability_id\x18\x03 \x01(\x05:\x02-1\"9\n\x10\x43\x44OTAMsg_MapLine\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\x0f\n\x07initial\x18\x03 \x01(\x08\"S\n\x12\x43\x44OTAMsg_WorldLine\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\t\n\x01z\x18\x03 \x01(\x05\x12\x0f\n\x07initial\x18\x04 \x01(\x08\x12\x0b\n\x03\x65nd\x18\x05 \x01(\x08\"\xd0\x01\n\x16\x43\x44OTAMsg_SendStatPopup\x12\x39\n\x05style\x18\x01 \x01(\x0e\x32\x14.EDOTAStatPopupTypes:\x14k_EDOTA_SPT_Textline\x12\x14\n\x0cstat_strings\x18\x02 \x03(\t\x12\x13\n\x0bstat_images\x18\x03 \x03(\x05\x12\x18\n\x10stat_image_types\x18\x04 \x03(\x05\x12\x10\n\x08\x64uration\x18\x05 \x01(\x02\x12\x10\n\x08use_html\x18\x06 \x01(\x08\x12\x12\n\nmovie_name\x18\x07 \x01(\t\"3\n\x1d\x43\x44OTAMsg_DismissAllStatPopups\x12\x12\n\ntime_delay\x18\x01 \x01(\x02\">\n\x15\x43\x44OTAMsg_CoachHUDPing\x12\t\n\x01x\x18\x01 \x01(\r\x12\t\n\x01y\x18\x02 \x01(\r\x12\x0f\n\x07tgtpath\x18\x03 \x01(\t\"\xda\x01\n\x12\x43\x44OTAMsg_UnitOrder\x12:\n\norder_type\x18\x02 \x01(\x0e\x32\x10.dotaunitorder_t:\x14\x44OTA_UNIT_ORDER_NONE\x12\r\n\x05units\x18\x03 \x03(\x05\x12\x17\n\x0ctarget_index\x18\x04 \x01(\x05:\x01\x30\x12\x19\n\rability_index\x18\x05 \x01(\x05:\x02-1\x12\x1d\n\x08position\x18\x06 \x01(\x0b\x32\x0b.CMsgVector\x12\x17\n\x0fsequence_number\x18\x08 \x01(\x05\x12\r\n\x05\x66lags\x18\t \x01(\r\"\xc1\x01\n\x18VersusScene_PlayActivity\x12:\n\nactivities\x18\x01 \x03(\x0b\x32&.VersusScene_PlayActivity.ActivityInfo\x12\x15\n\rplayback_rate\x18\x02 \x01(\x02\x1aR\n\x0c\x41\x63tivityInfo\x12\x10\n\x08\x61\x63tivity\x18\x01 \x01(\t\x12\x19\n\x11\x64isable_auto_kill\x18\x02 \x01(\x08\x12\x15\n\rforce_looping\x18\x03 \x01(\x08\"Q\n\x15VersusScene_ChatWheel\x12#\n\x0f\x63hat_message_id\x18\x01 \x01(\r:\n4294967295\x12\x13\n\x0b\x65moticon_id\x18\x02 \x01(\r\"(\n\x18VersusScene_PlaybackRate\x12\x0c\n\x04rate\x18\x01 \x01(\x02*v\n\x0b\x45PingSource\x12\x19\n\x15k_ePingSource_Default\x10\x00\x12\x19\n\x15k_ePingSource_Warning\x10\x01\x12\x17\n\x13k_ePingSource_Wheel\x10\x02\x12\x18\n\x14k_ePingSource_System\x10\x03*\xa4\x01\n\x13\x45\x44OTAStatPopupTypes\x12\x18\n\x14k_EDOTA_SPT_Textline\x10\x00\x12\x15\n\x11k_EDOTA_SPT_Basic\x10\x01\x12\x14\n\x10k_EDOTA_SPT_Poll\x10\x02\x12\x14\n\x10k_EDOTA_SPT_Grid\x10\x03\x12\x19\n\x15k_EDOTA_SPT_DualImage\x10\x04\x12\x15\n\x11k_EDOTA_SPT_Movie\x10\x05*\xd9\x0b\n\x0f\x64otaunitorder_t\x12\x18\n\x14\x44OTA_UNIT_ORDER_NONE\x10\x00\x12$\n DOTA_UNIT_ORDER_MOVE_TO_POSITION\x10\x01\x12\"\n\x1e\x44OTA_UNIT_ORDER_MOVE_TO_TARGET\x10\x02\x12\x1f\n\x1b\x44OTA_UNIT_ORDER_ATTACK_MOVE\x10\x03\x12!\n\x1d\x44OTA_UNIT_ORDER_ATTACK_TARGET\x10\x04\x12!\n\x1d\x44OTA_UNIT_ORDER_CAST_POSITION\x10\x05\x12\x1f\n\x1b\x44OTA_UNIT_ORDER_CAST_TARGET\x10\x06\x12$\n DOTA_UNIT_ORDER_CAST_TARGET_TREE\x10\x07\x12\"\n\x1e\x44OTA_UNIT_ORDER_CAST_NO_TARGET\x10\x08\x12\x1f\n\x1b\x44OTA_UNIT_ORDER_CAST_TOGGLE\x10\t\x12!\n\x1d\x44OTA_UNIT_ORDER_HOLD_POSITION\x10\n\x12!\n\x1d\x44OTA_UNIT_ORDER_TRAIN_ABILITY\x10\x0b\x12\x1d\n\x19\x44OTA_UNIT_ORDER_DROP_ITEM\x10\x0c\x12\x1d\n\x19\x44OTA_UNIT_ORDER_GIVE_ITEM\x10\r\x12\x1f\n\x1b\x44OTA_UNIT_ORDER_PICKUP_ITEM\x10\x0e\x12\x1f\n\x1b\x44OTA_UNIT_ORDER_PICKUP_RUNE\x10\x0f\x12!\n\x1d\x44OTA_UNIT_ORDER_PURCHASE_ITEM\x10\x10\x12\x1d\n\x19\x44OTA_UNIT_ORDER_SELL_ITEM\x10\x11\x12$\n DOTA_UNIT_ORDER_DISASSEMBLE_ITEM\x10\x12\x12\x1d\n\x19\x44OTA_UNIT_ORDER_MOVE_ITEM\x10\x13\x12$\n DOTA_UNIT_ORDER_CAST_TOGGLE_AUTO\x10\x14\x12\x18\n\x14\x44OTA_UNIT_ORDER_STOP\x10\x15\x12\x19\n\x15\x44OTA_UNIT_ORDER_TAUNT\x10\x16\x12\x1b\n\x17\x44OTA_UNIT_ORDER_BUYBACK\x10\x17\x12\x19\n\x15\x44OTA_UNIT_ORDER_GLYPH\x10\x18\x12)\n%DOTA_UNIT_ORDER_EJECT_ITEM_FROM_STASH\x10\x19\x12\x1d\n\x19\x44OTA_UNIT_ORDER_CAST_RUNE\x10\x1a\x12 \n\x1c\x44OTA_UNIT_ORDER_PING_ABILITY\x10\x1b\x12%\n!DOTA_UNIT_ORDER_MOVE_TO_DIRECTION\x10\x1c\x12\x1a\n\x16\x44OTA_UNIT_ORDER_PATROL\x10\x1d\x12*\n&DOTA_UNIT_ORDER_VECTOR_TARGET_POSITION\x10\x1e\x12\x19\n\x15\x44OTA_UNIT_ORDER_RADAR\x10\x1f\x12)\n%DOTA_UNIT_ORDER_SET_ITEM_COMBINE_LOCK\x10 \x12\x1c\n\x18\x44OTA_UNIT_ORDER_CONTINUE\x10!\x12*\n&DOTA_UNIT_ORDER_VECTOR_TARGET_CANCELED\x10\"\x12$\n DOTA_UNIT_ORDER_CAST_RIVER_PAINT\x10#\x12\x32\n.DOTA_UNIT_ORDER_PREGAME_ADJUST_ITEM_ASSIGNMENT\x10$\x12)\n%DOTA_UNIT_ORDER_DROP_ITEM_AT_FOUNTAIN\x10%\x12\x35\n1DOTA_UNIT_ORDER_TAKE_ITEM_FROM_NEUTRAL_ITEM_STASH\x10&\x12!\n\x1d\x44OTA_UNIT_ORDER_MOVE_RELATIVE\x10\'\x12#\n\x1f\x44OTA_UNIT_ORDER_CAST_TOGGLE_ALT\x10(\x12 \n\x1c\x44OTA_UNIT_ORDER_CONSUME_ITEM\x10)*\x8f\x01\n\x1e\x45\x44OTAVersusScenePlayerBehavior\x12$\n VS_PLAYER_BEHAVIOR_PLAY_ACTIVITY\x10\x01\x12!\n\x1dVS_PLAYER_BEHAVIOR_CHAT_WHEEL\x10\x02\x12$\n VS_PLAYER_BEHAVIOR_PLAYBACK_RATE\x10\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dota_commonmessages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EPINGSOURCE']._serialized_start=1313
  _globals['_EPINGSOURCE']._serialized_end=1431
  _globals['_EDOTASTATPOPUPTYPES']._serialized_start=1434
  _globals['_EDOTASTATPOPUPTYPES']._serialized_end=1598
  _globals['_DOTAUNITORDER_T']._serialized_start=1601
  _globals['_DOTAUNITORDER_T']._serialized_end=3098
  _globals['_EDOTAVERSUSSCENEPLAYERBEHAVIOR']._serialized_start=3101
  _globals['_EDOTAVERSUSSCENEPLAYERBEHAVIOR']._serialized_end=3244
  _globals['_CDOTAMSG_LOCATIONPING']._serialized_start=54
  _globals['_CDOTAMSG_LOCATIONPING']._serialized_end=224
  _globals['_CDOTAMSG_ITEMALERT']._serialized_start=226
  _globals['_CDOTAMSG_ITEMALERT']._serialized_end=297
  _globals['_CDOTAMSG_MAPLINE']._serialized_start=299
  _globals['_CDOTAMSG_MAPLINE']._serialized_end=356
  _globals['_CDOTAMSG_WORLDLINE']._serialized_start=358
  _globals['_CDOTAMSG_WORLDLINE']._serialized_end=441
  _globals['_CDOTAMSG_SENDSTATPOPUP']._serialized_start=444
  _globals['_CDOTAMSG_SENDSTATPOPUP']._serialized_end=652
  _globals['_CDOTAMSG_DISMISSALLSTATPOPUPS']._serialized_start=654
  _globals['_CDOTAMSG_DISMISSALLSTATPOPUPS']._serialized_end=705
  _globals['_CDOTAMSG_COACHHUDPING']._serialized_start=707
  _globals['_CDOTAMSG_COACHHUDPING']._serialized_end=769
  _globals['_CDOTAMSG_UNITORDER']._serialized_start=772
  _globals['_CDOTAMSG_UNITORDER']._serialized_end=990
  _globals['_VERSUSSCENE_PLAYACTIVITY']._serialized_start=993
  _globals['_VERSUSSCENE_PLAYACTIVITY']._serialized_end=1186
  _globals['_VERSUSSCENE_PLAYACTIVITY_ACTIVITYINFO']._serialized_start=1104
  _globals['_VERSUSSCENE_PLAYACTIVITY_ACTIVITYINFO']._serialized_end=1186
  _globals['_VERSUSSCENE_CHATWHEEL']._serialized_start=1188
  _globals['_VERSUSSCENE_CHATWHEEL']._serialized_end=1269
  _globals['_VERSUSSCENE_PLAYBACKRATE']._serialized_start=1271
  _globals['_VERSUSSCENE_PLAYBACKRATE']._serialized_end=1311
# @@protoc_insertion_point(module_scope)
