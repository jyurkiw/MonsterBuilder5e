from unittest import TestCase
from constants import MBKeys
from constants import StatKeys
from constants import Sizes
from constants import HitDice
from mb import Size
from mb import StatBonus
from assertpy import assert_that
from assertpy import fail


class TestSize(TestCase):
    def setUp(self) -> None:
        self.data = {}

    def test_setSize(self):
        data = self.data

        StatBonus.new_statblocks(data)
        StatBonus.set_stat_bonus(data, StatKeys.constitution, 3)
        Size.set_size(data, Sizes.medium)

        actual = data[MBKeys.size]
        expected = Sizes.medium

        assert_that(expected).is_equal_to(actual)

    def test_setNonExistentSize(self):
        data = self.data

        try:
            StatBonus.new_statblocks(data)
            StatBonus.set_stat_bonus(data, StatKeys.constitution, 3)
            Size.set_size(data, "flumph")
            fail(
                f'set_size("flumph") should have failed but did not. Size set to {data[MBKeys.size]}'
            )
        except Size.InvalidSizeException as ex:
            assert_that(type(ex)).is_equal_to(Size.InvalidSizeException)
        except Exception as gex:
            fail(f"Expected {type(Size.InvalidSizeException)} but found {type(gex)}")

    def test_setHDBySize(self):
        data = self.data

        StatBonus.new_statblocks(data)
        StatBonus.set_stat_bonus(data, StatKeys.constitution, 3)
        Size.set_size(data, Sizes.large)

        actual = data[MBKeys.hit_die]
        expected = HitDice[Sizes.large]

        assert_that(expected).is_equal_to(actual)

    def test_setAverageHPPerHDBySize(self):
        data = self.data

        StatBonus.new_statblocks(data)
        StatBonus.set_stat_bonus(data, StatKeys.constitution, 3)
        Size.set_size(data, Sizes.large)

        actual = data[MBKeys.average_hp_per_hd]
        expected = 8.5

        assert_that(expected).is_equal_to(actual)
