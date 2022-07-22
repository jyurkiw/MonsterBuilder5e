import math

from constants import MBKeys


class MinHPGTorEQMaxHPException(Exception):
    pass


def set_min_max_hp_and_hd(data, min_hp: int, max_hp: int):
    """
    Set the min and max hp and hd based on the minimum and maximum intended HP by DCV.
    :param data: The monster data
    :type data: dict
    :param min_hp: Minimum hp
    :type min_hp: int
    :param max_hp: Maximum hp
    :type max_hp: int
    """
    if min_hp >= max_hp:
        raise MinHPGTorEQMaxHPException(
            f"min_hp = {min_hp} vs max_hp = {max_hp}. Min should be less than max."
        )

    avg_hp_per_hd = data[MBKeys.average_hp_per_hd]
    data[MBKeys.minimum_target_hp] = min_hp
    data[MBKeys.maximum_target_hp] = max_hp

    data[MBKeys.minimum_hd] = math.floor(min_hp / avg_hp_per_hd) + 1
    data[MBKeys.maximum_hd] = math.ceil(max_hp / avg_hp_per_hd) - 1

    data[MBKeys.minimum_actual_hp] = math.floor(data[MBKeys.minimum_hd] * avg_hp_per_hd)
    data[MBKeys.maximum_actual_hp] = math.floor(data[MBKeys.maximum_hd] * avg_hp_per_hd)
