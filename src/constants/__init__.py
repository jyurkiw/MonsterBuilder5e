from dataclasses import dataclass

@dataclass
class MBKeys(object):
    combat_value: str = 'COMBAT_VALUE'
    offensive_combat_value: str = 'OFFENSIVE_COMBAT_VALUE'
    defensive_combat_value: str = 'DEFENSIVE_COMBAT_VALUE'
