from constants import MBKeys
import statistics


def calculate_combat_value(data: dict) -> int:
    """
    CV is the average of OCV and DCV, rounded.
    :param data: Monster data
    :type data: dict
    :return: Combat Value
    :rtype: int
    """
    data[MBKeys.combat_value] = round(
        statistics.mean(
            [
                data.get(MBKeys.offensive_combat_value, 0),
                data.get(MBKeys.defensive_combat_value, 0),
            ]
        )
    )

