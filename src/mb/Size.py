from constants import MBKeys
from constants import validate_size


class InvalidSizeException(Exception):
    pass


def set_size(data, size):
    if validate_size(size):
        data[MBKeys.size] = size
    else:
        raise InvalidSizeException(f'{size} is not a valid size')
