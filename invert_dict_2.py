#!/usr/bin/env python3
"""
Does the same as invert_dict
"""


d = {'apple': 1, 'banana': 2, 'orange': 3, 'grape': 2}
result = dict()
for key in d:
    val = d[key]
    if val not in result:
        result[val] = [key]
    else:
        result[val].append(key)

print(result)
