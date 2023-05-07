#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: test_lambda.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python test_lambda.py
"""

def add1(n1, n2):
    return n1 + n2

add2 = lambda n1, n2: n1 + n2

print(add1(5, 8))
print(add2(8, 5))
'''
13
13
'''