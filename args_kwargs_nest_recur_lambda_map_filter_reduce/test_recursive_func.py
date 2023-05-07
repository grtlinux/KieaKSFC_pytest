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

def count(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n, end=', ')
        count(n-1)

def sum(n):
    if n > 0:
        return n + sum(n-1)
    else:
        return 0
    
print('count:', count(10))
print('sum:', sum(10))
'''
10, 9, 8, 7, 6, 5, 4, 3, 2, 1, Blastoff!
count: None
sum: 55
'''