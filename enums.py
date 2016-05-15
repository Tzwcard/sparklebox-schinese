def enum(kv):
    i = iter(kv)
    dic = dict(zip(i, i))

    def f(key):
        return dic.get(key, "<missing string: {0}>".format(key))
    return f

rarity = enum([
    1, "Normal",
    2, "Normal+",
    3, "Rare",
    4, "Rare+",
    5, "SR",
    6, "SR+",
    7, "SSR",
    8, "SSR+",
])

attribute = enum([
    1, "Cute",
    2, "Cool",
    3, "Passion",
    4, "Office",
])

skill_type = enum([
    1, "PERFECT分数加成",
    2, "PERFECT/GREAT分数加成",
    4, "COMBO加成",
    5, "GREAT改PERFECT",
    6, "GREAT/NICE改PERFECT",
    7, "GREAT/NICE/BAD改PERFECT",
    9, "COMBO不中断",
    12, "锁血",
    14, "过载",
    17, "恢复生命",
])

skill_probability = enum([
    2, "小概率",
    3, "中概率",
    4, "高概率",
])

skill_length_type = enum([
    1, "一瞬间",
    2, "较短时间",
    3, "短时间",
    4, "稍长时间",
    5, "较长时间",
])

lskill_target = enum([
    1, "所有Cute",
    2, "所有Cool",
    3, "所有Passion",
    4, "所有",
])

lskill_effective_target = enum([
    1, "ca_cute",
    2, "ca_cool",
    3, "ca_passion",
    4, "ca_all",
])

lskill_param = enum([
    1, "Vocal表现值",
    2, "Visual表现值",
    3, "Dance表现值",
    4, "全表现值",
    5, "生命",
    6, "技能发动概率",
])

lskill_effective_param = enum([
    1, "ce_vocal",
    2, "ce_visual",
    3, "ce_dance",
    4, "ce_anyappeal",
    5, "ce_life",
    6, "ce_skill",
])

api_char_type = enum([
    1, "cute",
    2, "cool",
    3, "passion",
    4, "office"
])

lskill_target_attr = enum([
    1, "cute",
    2, "cool",
    3, "passion",
    4, "all",
])

lskill_target_param = enum([
    1, "vocal",
    2, "visual",
    3, "dance",
    4, "all",
    5, "life",
    6, "skill_probability",
])

skill_class = enum([
    1, "s_scorebonus",
    17, "s_heal",
    4, "s_combobonus",
    5, "s_pl",
    9, "s_cprot",
    7, "s_pl",
    2, "s_scorebonus",
    6, "s_pl",
    12, "s_life",
    14, "s_overload",
])

stat_dot = enum([
    1, "m_vi",
    2, "m_da",
    3, "m_vo"
])

stat_en = enum([
    1, "This card's highest stat is Visual",
    2, "This card's highest stat is Dance",
    3, "This card's highest stat is Vocal"
])

# TODO need enum defs for
# constellation
# blood_type
# hand
# personality
# home_town
