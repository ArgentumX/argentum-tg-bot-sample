import math

from errors.api_error import ApiError


def get_int(arg: str) -> int:
    if not arg.isnumeric():
        raise ApiError.validation_error("Ошибка валидации - введите число")
    return int(arg)


def get_float(arg: str) -> float:
    if not arg.replace(".", "", 1).isnumeric():
        raise ApiError.validation_error("Ошибка валидации - введите число")
    return float(arg)


def between(x: int | float, minimum: float = -math.inf, maximum: float = +math.inf):
    return minimum <= x <= maximum
