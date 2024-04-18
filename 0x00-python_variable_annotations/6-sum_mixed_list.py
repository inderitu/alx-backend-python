#!/usr/bin/env python3

"""
module that creates function sum_mixed_list

Write a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers andfloats
returns their sum as a float.

ensure input is list type
>>> sum_mixed_list("abc")
Traceback (most recent call last):
    ...
TypeError: mxd_lst must be a list

ensure input list has only ints and floats
>>> sum_mixed_list([1, 2.4, "d"])
Traceback (most recent call last):
    ...
TypeError: mxd_lst must contain only int and floats

ensure correct output
>>> print(sum_mixed_list([1, 2.4]))
3.4

correct output type
>>> isinstance(sum_mixed_list([1, 1]), float)
True

"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    returns total sum of numbers in mxd_lst
    """
    total: float = 0.0

    if isinstance(mxd_lst, list) is not True:
        raise TypeError("mxd_lst must be a list")
    for x in mxd_lst:
        if isinstance(x, int | float) is not True:
            raise TypeError("mxd_lst must contain only int and floats")
        total += x

    return total


if __name__ == "__main__":
    import doctest
    doctest.testmod()
