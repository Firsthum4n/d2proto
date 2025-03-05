import dota_modifiers_pb2

# Создаём объект
modifier_entry = dota_modifiers_pb2.CDOTAModifierBuffTableEntry()
modifier_entry.entry_type = dota_modifiers_pb2.DOTA_MODIFIER_ENTRY_TYPE.DOTA_MODIFIER_ENTRY_TYPE_ACTIVE
modifier_entry.stack_count = 3
modifier_entry.creation_time = 123.456

# Выводим объект
print(modifier_entry)