from constants import MBKeys
from constants import StatKeys


def _set_statblock(data, key):
    data[key] = {key: 0 for key in StatKeys.all_keys}


def new_statblocks(data):
    _set_statblock(data, MBKeys.stat_scores)
    _set_statblock(data, MBKeys.stat_bonuses)


def calculate_stat_scores(data):
    for key, value in data[MBKeys.stat_bonuses].items():
        data[MBKeys.stat_scores][key] = (value * 2) + 11
