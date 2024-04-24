import construct as c

sector_footer = c.Struct(
    'sector_id' / c.Int16ul,
    'checksum' / c.Int16ul,  # TODO calculate
    'signature' / c.Const(b'\x25\x20\x01\x08'),
    'counter' / c.Int32ul,
)

save_sector = c.Struct(
    'data' / c.Array(3968, c.Byte),
    'footer' / sector_footer,
)

battle_tower_pokemon = c.Struct(
    'species' / c.Int16ul,
    'held_item' / c.Int16ul,
    'moves' / c.Array(4, c.Int16ul),
    'level' / c.Int8ul,
    'pp_bonuses' / c.Int8ul,
    'ev_hp' / c.Int8ul,
    'ev_attack' / c.Int8ul,
    'ev_defense' / c.Int8ul,
    'ev_speed' / c.Int8ul,
    'ev_special_attack' / c.Int8ul,
    'ev_special_defense' / c.Int8ul,
    'ot_id' / c.Int32ul,
    'ivs_ability' / c.BitStruct(
        'hp' / c.BitsInteger(5),
        'attack' / c.BitsInteger(5),
        'defense' / c.BitsInteger(5),
        'speed' / c.BitsInteger(5),
        'special_attack' / c.BitsInteger(5),
        'special_defense' / c.BitsInteger(5),
        'gap' / c.Padding(1),
        'ability' / c.Bit,
    ),
    'personality' / c.Int32ul,
    'nickname' / c.Array(11, c.Byte),  # TODO string adapter
    'friendship' / c.Int8ul,
)

trainer_hill = c.Struct(
    'guardian' / c.Const(b'\x9d\xb3'),
    'n_trainers' / c.Int8ul,
    'id' / c.Int8ul,
    'dummy' / c.Int16ul,
    'checksum' / c.Int32ul,  # TODO calculate
    'trainers' / c.Array(6, c.Struct(
        'num' / c.Int8ul,
        'name' / c.Array(11, c.Byte),  # TODO string adapter
        'facility_class' / c.Int8ul,
        'unknown' / c.Int32ul,
        'speech_before' / c.Array(6, c.Int16ul),  # TODO map speech tokens
        'speech_win' / c.Array(6, c.Int16ul),
        'speech_lose' / c.Array(6, c.Int16ul),
        'speech_after' / c.Array(6, c.Int16ul),
        'party' / c.Array(6, battle_tower_pokemon),
    )),
    'footer' / sector_footer,
)

recorded_battle = c.Struct(
    'footer' / sector_footer,
)

file_struct = c.Struct(
    'save_a' / c.Array(14, save_sector),
    'save_b' / c.Array(14, save_sector),
    'hall_of_fame' / c.Array(2, save_sector),
    'trainer_hill' / trainer_hill,
    'recorded_battle' / save_sector,
)
