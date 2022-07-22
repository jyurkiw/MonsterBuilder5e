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
