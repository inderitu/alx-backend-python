#!/usr/bin/env python3

"""
Write a type-annotated function to_kv
takes a string k and an int OR float v as arguments
returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v annotated as a float.

ensure inputs are of correct types
>>> to_kv(2, 2)
Traceback (most recent call last):
    ...
TypeError: k must be a string

>>> to_kv("test", "test")
Traceback (most recent call last):
    ...
TypeError: v must be an int or float
"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    returns tuple (k, v *v)
    """
    if isinstance(k, str) is not True:
        raise TypeError("k must be a string")
    if isinstance(v, int | float) is not True:
        raise TypeError("v must be an int or float")

    return (k, v * v)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
