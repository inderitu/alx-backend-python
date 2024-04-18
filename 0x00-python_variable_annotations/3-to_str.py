#!/usr/bin/env python3

"""
module that defines function to_str

check correct output
>>> print(to_str(3.14))
3.14

ensure output is type string
>>> isinstance(to_str(3.14), str)
True

check input is of type float
>>> to_str(3)
Traceback (most recent call last):
    ...
TypeError: n must be of type float
"""


def to_str(n: float) -> str:
    """
    returns string reprensentation of n
    """
    if isinstance(n, float) is not True:
        raise TypeError("n must be of type float")

    return f"{n}"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
