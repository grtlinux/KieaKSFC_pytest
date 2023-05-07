#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: test_multireturn.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python test_multireturn.py
"""

def plus_minus(a, b):
    return a+b, a-b

result = plus_minus(10, 5)
print(type(result), result)

r1, r2 = plus_minus(10, 5)
print(r1, r2)
'''
<class 'tuple'> (15, 5)
15 5
'''