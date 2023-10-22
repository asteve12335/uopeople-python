#!/usr/bin/env python3

"""
Write a function called nested_sum that takes a
list of lists of integers and adds up
the elements from all of the nested lists. For example:

>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
"""


def nested_sum(t: list):
    total = 0
    for item in t:
        if isinstance(item, list):
            total += sum(item)
            continue
        total += item
    return total
