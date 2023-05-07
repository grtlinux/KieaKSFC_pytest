#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: test_nested_func.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python test_nested_func.py
"""

def func1(n1, n2):
    def func2(n3, n4):
        return n3 + n4
    return func2(n1, n2)

print(func1(1, 2))
'''
3
'''