#!/usr/bin/env python3

"""
module that defines a concat function
Write a type-annotated function concat that takes a string str1
and a string str2 as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    return a concatenated str1 and str2

    ensure str1 is a string
    >>> concat(1, "test")
    Traceback (most recent call last):
        ...
    TypeError: str1 must be a string

    ensure str1 is a string
    >>> concat("test", 1)
    Traceback (most recent call last):
        ...
    TypeError: str2 must be a string

    check correct return
    >>> print(concat("abc", "abc"))
    abcabc
    """

    if isinstance(str1, str) is not True:
        raise TypeError("str1 must be a string")
    if isinstance(str2, str) is not True:
        raise TypeError("str2 must be a string")

    return f"{str1}{str2}"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
