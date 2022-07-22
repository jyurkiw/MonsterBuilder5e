from constants import MBKeys
from constants import validate_size


class InvalidSizeException(Exception):
    def __int__(self, size):
        super().__init__(f'{size} is not a valid size')


def set_size(data, size):
    if validate_size(size):
        data[MBKeys.size] = size
    else:
        raise InvalidSizeException(size)
