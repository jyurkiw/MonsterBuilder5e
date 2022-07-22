import math
from unittest import TestCase
from assertpy import assert_that
from assertpy import fail
from constants import MBKeys
from constants import StatKeys
from constants import Sizes

from mb import StatBonus
from mb import Size
from mb import HitPoints


class TestHitPoints(TestCase):
    def setUp(self) -> None:
        data = {}
        StatBonus.new_statblocks(data)
        StatBonus.set_stat_bonus(data, StatKeys.constitution, 3)
        Size.set_size(data, Sizes.large)
        HitPoints.set_min_max_hp_and_hd(data, 100, 200)
        self.data = data

    def test_min_hp(self):
        data = self.data

        expected = 100
        actual = data[MBKeys.minimum_target_hp]

        assert_that(expected).is_equal_to(actual)

    def test_max_hp(self):
        data = self.data

        expected = 200
        actual = data[MBKeys.maximum_target_hp]

        assert_that(expected).is_equal_to(actual)

    def test_min_hd(self):
        data = self.data

        expected = math.floor(100 / 8.5) + 1
        actual = data[MBKeys.minimum_hd]

        assert_that(expected).is_equal_to(actual)

    def test_max_hd(self):
        data = self.data

        expected = math.ceil(200 / 8.5) - 1
        actual = data[MBKeys.maximum_hd]

        assert_that(expected).is_equal_to(actual)

    def test_min_actual_hp(self):
        data = self.data

        expected = math.floor(data[MBKeys.minimum_hd] * 8.5)
        actual = data[MBKeys.minimum_actual_hp]

        assert_that(expected).is_equal_to(actual)

    def test_max_actual_hp(self):
        data = self.data

        expected = math.floor(data[MBKeys.maximum_hd] * 8.5)
        actual = data[MBKeys.maximum_actual_hp]

        assert_that(expected).is_equal_to(actual)

    def test_min_actual_hp_gteq_min_target_hp(self):
        data = self.data

        expected = data[MBKeys.minimum_actual_hp]
        actual = data[MBKeys.minimum_target_hp]

        assert_that(expected).is_greater_than_or_equal_to(actual)

    def test_max_actual_hp_lteq_min_target_hp(self):
        data = self.data

        expected = data[MBKeys.maximum_actual_hp]
        actual = data[MBKeys.maximum_target_hp]

        assert_that(expected).is_less_than_or_equal_to(actual)


class TestMinHigherThanMax(TestCase):
    def setUp(self) -> None:
        data = {}
        StatBonus.new_statblocks(data)
        StatBonus.set_stat_bonus(data, StatKeys.constitution, 3)
        Size.set_size(data, Sizes.large)
        self.data = data

    def test_min_higher_than_max(self):
        data = self.data

        try:
            HitPoints.set_min_max_hp_and_hd(data, 200, 100)
            fail('No exception raised')
        except HitPoints.MinHPGTorEQMaxHPException as mex:
            assert_that(type(mex)).is_equal_to(HitPoints.MinHPGTorEQMaxHPException)
        except Exception as ex:
            fail(f'Unexpected exception type raised: {type(ex)}')
