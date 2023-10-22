#!/usr/bin/env python3

"""
Write a function called cumsum that takes a list of numbers
and returns the cumulative sum; that is, a new list where
the ith element is the sum of the first i + 1 elements from
the original list. For example:

>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
"""


def cumsum(t: list):
    copy_t = t[:]
    cum_list = [copy_t[0]]

    for i in range(1, len(copy_t)):
        cum_list.append(sum(copy_t[:i + 1]))

    return cum_list
