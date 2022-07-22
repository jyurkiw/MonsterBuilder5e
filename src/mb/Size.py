from constants import MBKeys
from constants import StatKeys
from constants import validate_size
from constants import HitDice


class InvalidSizeException(Exception):
    pass


def set_size(data, size):
    """
    Set the monster's size.
    Also sets HD and average HP per HD.

    :param data: Monster data
    :type data: dict
    :param size: Monster size
    :type size: str
    """
    if validate_size(size):
        data[MBKeys.size] = size
        data[MBKeys.hit_die] = HitDice[size]
        data[MBKeys.average_hp_per_hd] = float(
            round(HitDice[size] / 2)
            + data[MBKeys.stat_bonuses][StatKeys.constitution]
            + 0.5
        )
    else:
        raise InvalidSizeException(f"{size} is not a valid size")
