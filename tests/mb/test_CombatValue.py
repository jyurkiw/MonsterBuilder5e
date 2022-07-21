import unittest
from constants import MBKeys
from assertpy import assert_that
from mb.CombatValue import calculate_combat_value


class test_CombatValue(unittest.TestCase):
    def test_noOCV(self):
        data = {MBKeys.defensive_combat_value: 2}
        calculate_combat_value(data)

        actual = data[MBKeys.combat_value]
        expected = round((2 + 0)/2)
        assert_that(actual).is_equal_to(expected)

    def test_noDCV(self):
        data = {MBKeys.offensive_combat_value: 2}
        calculate_combat_value(data)

        actual = data[MBKeys.combat_value]
        expected = round((2 + 0) / 2)
        assert_that(actual).is_equal_to(expected)

    def test_OCVandDCV(self):
        data = {MBKeys.defensive_combat_value: 2, MBKeys.offensive_combat_value: 4}
        calculate_combat_value(data)

        actual = data[MBKeys.combat_value]
        expected = round((2 + 4) / 2)
        assert_that(actual).is_equal_to(expected)
