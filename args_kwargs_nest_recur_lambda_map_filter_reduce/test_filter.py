#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: test_recursive_func.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python test_recursive_func.py
"""

lst = range(10)
lst_even = list(filter(lambda x: x % 2 == 0, lst))
print('even:', lst_even)
lst_odd = list(filter(lambda x: x % 2 == 1, lst))
print('odd:', lst_odd)

'''
'''