#!/usr/bin/env python3

"""
module that defines a floor function

>>> print(floor(3.14))
3
"""
import math


def floor(n: float) -> int:
    """
    float n as argument and returns the floor of the float.

    check n is of type float
    >>> floor(3)
    Traceback (most recent call last):
        ...
    TypeError: n must be of type float

    >>> floor("string")
    Traceback (most recent call last):
        ...
    TypeError: n must be of type float


    check for correct output
    >>> print(floor(3.14))
    3
    """
    if isinstance(n, float) is not True:
        raise TypeError("n must be of type float")
    return math.floor(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
