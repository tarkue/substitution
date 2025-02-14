import math

from typing import Iterable
from functools import reduce


def lcm(a: int, b: int) -> int:
    """
    Calculates the LCM of two numbers.
    """
    return abs(a * b) // math.gcd(a, b)


def lcm_multiple(numbers: Iterable[int]) -> int:
    """
    Calculates the LCM of a list of numbers.
    """
    return reduce(lcm, numbers)
