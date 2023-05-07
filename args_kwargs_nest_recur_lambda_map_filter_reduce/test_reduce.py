#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: test_reduce.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python test_reduce.py
"""
import functools

lst = list(range(10))
print(lst)

sum = functools.reduce(lambda x, y: x + y, lst)
print('sum:', sum)
len = functools.reduce(lambda x, y: x + 1, lst, 0)
print('len:', len)
max = functools.reduce(lambda x, y: x if x > y else y, lst)
print('max:', max)
min = functools.reduce(lambda x, y: x if x < y else y, lst)
print('min:', min)
'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sum: 45
len: 10
max: 9
min: 0
'''