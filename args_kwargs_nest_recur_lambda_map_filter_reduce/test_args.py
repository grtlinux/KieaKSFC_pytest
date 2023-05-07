#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: test_args.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python test_args.py
"""

def sum(*args):
    print(type(args), args)
    result = 0
    for i in args:
        result += i
    return result

print(sum(1, 2, 3, 4, 5))
'''
<class 'tuple'> (1, 2, 3, 4, 5)
15
'''