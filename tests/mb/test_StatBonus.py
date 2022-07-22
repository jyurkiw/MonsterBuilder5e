from constants import MBKeys
from constants import StatKeys
from unittest import TestCase
from assertpy import assert_that
from mb import StatBonus


class TestNewStatBlocks(TestCase):
    def setUp(self) -> None:
        self.data = {}
        StatBonus.new_statblocks(self.data)

    def test_new_statscore_StrengthZero(self):
        data = self.data

        actual = data[MBKeys.stat_scores][StatKeys.strength]
        expected = 0

        assert_that(actual).is_equal_to(expected)

    def test_new_statscore_DexterityZero(self):
        data = self.data

        actual = data[MBKeys.stat_scores][StatKeys.dexterity]
        expected = 0

        assert_that(actual).is_equal_to(expected)

    def test_new_statscore_ConstitutionZero(self):
        data = self.data

        actual = data[MBKeys.stat_scores][StatKeys.constitution]
        expected = 0

        assert_that(actual).is_equal_to(expected)

    def test_new_statscore_IntelligenceZero(self):
        data = self.data

        actual = data[MBKeys.stat_scores][StatKeys.intelligence]
        expected = 0

        assert_that(actual).is_equal_to(expected)

    def test_new_statscore_WisdomZero(self):
        data = self.data

        actual = data[MBKeys.stat_scores][StatKeys.wisdom]
        expected = 0

        assert_that(actual).is_equal_to(expected)

    def test_new_statscore_CharismaZero(self):
        data = self.data

        actual = data[MBKeys.stat_scores][StatKeys.charisma]
        expected = 0

        assert_that(actual).is_equal_to(expected)

    def test_new_statbonus_StrengthZero(self):
        data = self.data

        actual = data[MBKeys.stat_bonuses][StatKeys.strength]
        expected = 0

        assert_that(actual).is_equal_to(expected)

    def test_new_statbonus_DexterityZero(self):
        data = self.data

        actual = data[MBKeys.stat_bonuses][StatKeys.dexterity]
        expected = 0

        assert_that(actual).is_equal_to(expected)

    def test_new_statbonus_ConstitutionZero(self):
        data = self.data

        actual = data[MBKeys.stat_bonuses][StatKeys.constitution]
        expected = 0

        assert_that(actual).is_equal_to(expected)

    def test_new_statbonus_IntelligenceZero(self):
        data = self.data

        actual = data[MBKeys.stat_bonuses][StatKeys.intelligence]
        expected = 0

        assert_that(actual).is_equal_to(expected)

    def test_new_statbonus_WisdomZero(self):
        data = self.data

        actual = data[MBKeys.stat_bonuses][StatKeys.wisdom]
        expected = 0

        assert_that(actual).is_equal_to(expected)

    def test_new_statbonus_CharismaZero(self):
        data = self.data

        actual = data[MBKeys.stat_bonuses][StatKeys.charisma]
        expected = 0

        assert_that(actual).is_equal_to(expected)


class TestCalculateStatScores(TestCase):
    def setUp(self) -> None:
        self.data = {}
        StatBonus.new_statblocks(self.data)

        self.data[MBKeys.stat_bonuses][StatKeys.strength] = 1
        self.data[MBKeys.stat_bonuses][StatKeys.dexterity] = 2
        self.data[MBKeys.stat_bonuses][StatKeys.constitution] = 3
        self.data[MBKeys.stat_bonuses][StatKeys.intelligence] = 4
        self.data[MBKeys.stat_bonuses][StatKeys.wisdom] = 5
        self.data[MBKeys.stat_bonuses][StatKeys.charisma] = 6

        StatBonus.calculate_stat_scores(self.data)

    def test_calculate_strength_score(self):
        data = self.data

        actual = data[MBKeys.stat_scores][StatKeys.strength]
        expected = 13

        assert_that(actual).is_equal_to(expected)

    def test_calculate_dexterity_score(self):
        data = self.data

        actual = data[MBKeys.stat_scores][StatKeys.dexterity]
        expected = 15

        assert_that(actual).is_equal_to(expected)

    def test_calculate_constitution_score(self):
        data = self.data

        actual = data[MBKeys.stat_scores][StatKeys.constitution]
        expected = 17

        assert_that(actual).is_equal_to(expected)

    def test_calculate_intelligence_score(self):
        data = self.data

        actual = data[MBKeys.stat_scores][StatKeys.intelligence]
        expected = 19

        assert_that(actual).is_equal_to(expected)

    def test_calculate_wisdom_score(self):
        data = self.data

        actual = data[MBKeys.stat_scores][StatKeys.wisdom]
        expected = 21

        assert_that(actual).is_equal_to(expected)

    def test_calculate_charisma_score(self):
        data = self.data

        actual = data[MBKeys.stat_scores][StatKeys.charisma]
        expected = 23

        assert_that(actual).is_equal_to(expected)
