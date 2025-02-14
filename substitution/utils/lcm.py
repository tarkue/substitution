import math
from functools import reduce


def lcm(a, b):
    """Вычисляет НОК для двух чисел."""
    return abs(a * b) // math.gcd(a, b)


def lcm_multiple(numbers):
    """Вычисляет НОК для списка чисел."""
    return reduce(lcm, numbers)
