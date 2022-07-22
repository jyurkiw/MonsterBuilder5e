from dataclasses import dataclass
from dataclasses import fields


def all_values(t: type):
    """
    Get all field values from a constants class.
    :param t: constants class type
    :type t: type
    :return: List of values
    :rtype: [str]
    """
    return [f.default for f in fields(t)]


@dataclass
class MBKeys(object):
    combat_value: str = "COMBAT_VALUE"
    offensive_combat_value: str = "OFFENSIVE_COMBAT_VALUE"
    defensive_combat_value: str = "DEFENSIVE_COMBAT_VALUE"

    stat_bonuses: str = "STAT_BONUSES"
    stat_scores: str = "STAT_SCORES"

    size: str = "SIZE"
    hit_die: str = "HIT_DIE"
    average_hp_per_hd: str = "AVERAGE_HP_PER_HD"
    maximum_target_hp: str = 'MAXIMUM_TARGET_HP'
    minimum_target_hp: str = 'MINIMUM_TARGET_HP'
    maximum_actual_hp: str = 'MAXIMUM_ACTUAL_HP'
    minimum_actual_hp: str = 'MINIMUM_ACTUAL_HP'
    maximum_hd: str = 'MAXIMUM_HD'
    minimum_hd: str = 'MINIMUM_HD'


@dataclass
class StatKeys(object):
    strength: str = "STRENGTH"
    dexterity: str = "DEXTERITY"
    constitution: str = "CONSTITUTION"
    intelligence: str = "INTELLIGENCE"
    wisdom: str = "WISDOM"
    charisma: str = "CHARISMA"


@dataclass
class Sizes(object):
    tiny: str = "Tiny"
    small: str = "Small"
    medium: str = "Medium"
    large: str = "Large"
    huge: str = "Huge"
    gargantuan: str = "Gargantuan"


_size_set = set(all_values(Sizes))


def validate_size(size):
    return size in _size_set


HitDice = {
    Sizes.tiny: 4,
    Sizes.small: 6,
    Sizes.medium: 8,
    Sizes.large: 10,
    Sizes.huge: 12,
    Sizes.gargantuan: 20,
}


_hd_set = set([v for v in HitDice.values()])


def validate_hd(hd):
    return hd in _hd_set
