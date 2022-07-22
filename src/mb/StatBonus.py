from constants import MBKeys
from constants import StatKeys
from constants import all_values


def _set_statblock(data, key):
    data[key] = {key: 0 for key in all_values(StatKeys)}


def set_stat_bonus(data, key, value: int):
    """
    Set a stat bonus to a given value.
    :param data: The monster data
    :type data: dict
    :param key: The stat key
    :type key: str
    :param value: The bonus value
    :type value: int
    """
    data[MBKeys.stat_bonuses][key] = int(value)


def get_stat_bonus(data, key):
    """
    Get a stat bonus.
    :param data: The monster data
    :type data: dict
    :param key: The stat bonus key
    :type key: str
    :return: The stat bonus
    :rtype: int
    """
    return int(data[MBKeys.stat_bonuses][key])


def new_statblocks(data):
    """
    Set up new statblocks for bonuses and stat values
    :param data: The monster data
    :type data: dict
    """
    _set_statblock(data, MBKeys.stat_scores)
    _set_statblock(data, MBKeys.stat_bonuses)


def calculate_stat_scores(data):
    """
    Calculate stat scores based on their bonuses
    :param data: The monster data
    :type data: dict
    """
    for key, value in data[MBKeys.stat_bonuses].items():
        data[MBKeys.stat_scores][key] = (value * 2) + 11
