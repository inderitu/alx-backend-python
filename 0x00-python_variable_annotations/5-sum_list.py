#!/usr/bin/env python3

"""
module that defines function sum_list
Write a type-annotated function sum_list
which takes a list input_list of floats as argument
returns their sum as a float.

ensure input_list is of type list
>>> sum_list(3)
Traceback (most recent call last):
    ...
TypeError: input_list must be a list

>>> sum_list("string")
Traceback (most recent call last):
    ...
TypeError: input_list must be a list

ensure input_list contains only floats
>>> sum_list([1.2, 3])
Traceback (most recent call last):
    ...
TypeError: input_list must contain only floats

check for correct output
>>> print(sum_list([1.1, 2.1]))
3.2

check for float return type
>>> isinstance(sum_list([1.1, 1.2]), float)
True
"""


def sum_list(input_list: list[float]) -> float:
    """
    returns sum of floats in input_list
    """
    total: float = 0.0

    if isinstance(input_list, list) is not True:
        raise TypeError("input_list must be a list")

    for x in input_list:
        if isinstance(x, float) is not True:
            raise TypeError("input_list must contain only floats")
        total += x

    return total


if __name__ == "__main__":
    import doctest
    doctest.testmod()
