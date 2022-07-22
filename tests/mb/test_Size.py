from unittest import TestCase
from constants import MBKeys
from constants import Sizes
from mb import Size
from assertpy import assert_that
from assertpy import fail


class Test_Size(TestCase):
    def setUp(self) -> None:
        self.data = {}

    def test_setSize(self):
        data = self.data

        Size.set_size(data, Sizes.medium)

        actual = data[MBKeys.size]
        expected = Sizes.medium

        assert_that(expected).is_equal_to(actual)

    def test_setNonExistentSize(self):
        data = self.data

        try:
            Size.set_size(data, 'flumph')
            fail(f'set_size("flumph") should have failed but did not. Size set to {data[MBKeys.size]}')
        except Size.InvalidSizeException as ex:
            assert_that(type(ex)).is_equal_to(Size.InvalidSizeException)
        except Exception as gex:
            fail(f'Expected {type(Size.InvalidSizeException)} but found {type(gex)}')
