#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: test_map.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python test_map.py
"""

lst1 = [1, 2, 3, 4, 5]
square = lambda x: x**2
lst2 = list(map(square, lst1))
print(lst2)

lst3 = list(map(lambda n1, n2: n1 + n2, lst1, lst2))
print(lst3)
'''
[1, 4, 9, 16, 25]
[2, 6, 12, 20, 30]
'''