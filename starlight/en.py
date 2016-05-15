import csvloader
import functools
import os
import enums
import re

# skill describer

SKILL_DESCRIPTIONS = {
    1: """使所有PERFECT音符获得 <span class="let">{0}</span>% 的分数加成""",
    2: """使所有PERFECT/GREAT音符获得 <span class="let">{0}</span>% 的分数加成""",
    4: """获得额外的 <span class="let">{0}</span>% 的COMBO加成""",
    5: """使所有GREAT音符改判为PERFECT""",
    6: """使所有GREAT/NICE音符改判为PERFECT""",
    7: """使所有GREAT/NICE/BAD音符改判为PERFECT""",
    9: """使NICE音符不会中断COMBO""",
    12: """使你的生命不会减少""",
    14: """消耗 <span class="let">{1}</span> 生命，PERFECT音符获得 <span class="let">{0}</span>% 的分数加成，并且NICE/BAD音符不会中断COMBO""",
    17: """使所有PERFECT音符恢复你 <span class="let">{0}</span> 点生命""" }

REMOVE_HTML = re.compile(r"</?span[^>]*>")

def describe_skill(skill):
    return REMOVE_HTML.sub("", describe_skill_html(skill))

def describe_lead_skill(lskill):
    return REMOVE_HTML.sub("", describe_lead_skill_html(lskill))

def describe_skill_html(skill):
    fire_interval = skill.condition
    effect_val = skill.value
    # TODO symbols
    if skill.skill_type in [1, 2, 4, 14]:
        effect_val -= 100

    effect_clause = SKILL_DESCRIPTIONS.get(
        skill.skill_type, "").format(effect_val, skill.skill_trigger_value)
    interval_clause = """每 <span class="let">{0}</span> 秒，""".format(
        fire_interval)
    probability_clause = """有 <span class="var">{0}</span>% 的几率""".format(
        skill.chance())
    length_clause = """，持续 <span class="var">{0}</span> 秒。""".format(
        skill.dur())

    return " ".join((interval_clause, probability_clause, effect_clause, length_clause))


def describe_lead_skill_html(skill):
    assert skill.up_type == 1 and skill.type == 20

    target_attr = enums.lskill_target(skill.target_attribute)
    target_param = enums.lskill_param(skill.target_param)

    built = """提升所有 {1} 偶像的 {0} <span class="let">{2}</span>%。""".format(
        target_param, target_attr, skill.up_value)
    return built
