from dataclasses import dataclass
from dataclasses import field


@dataclass
class MBKeys(object):
    combat_value: str = "COMBAT_VALUE"
    offensive_combat_value: str = "OFFENSIVE_COMBAT_VALUE"
    defensive_combat_value: str = "DEFENSIVE_COMBAT_VALUE"

    stat_bonuses: str = "STAT_BONUSES"
    stat_scores: str = "STAT_SCORES"


@dataclass
class StatKeys(object):
    strength: str = "STRENGTH"
    dexterity: str = "DEXTERITY"
    constitution: str = "CONSTITUTION"
    intelligence: str = "INTELLIGENCE"
    wisdom: str = "WISDOM"
    charisma: str = "CHARISMA"

    all_keys: tuple = (
            "STRENGTH",
            "DEXTERITY",
            "CONSTITUTION",
            "INTELLIGENCE",
            "WISDOM",
            "CHARISMA",
    )
