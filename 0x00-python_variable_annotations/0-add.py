#!/usr/bin/env python3

"""
module that defines an add function
add takes a float a and a float b
add returns sum as a float

>>> add(1.5, 2.5)
4.0
"""


def add(a: float, b: float) -> float:
    """
    returns sum of float and float b
    """

    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
