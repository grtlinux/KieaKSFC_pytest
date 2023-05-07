#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: test_kwargs.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python test_kwargs.py
"""

def info_kwargs(**kwargs):
    print(type(kwargs), kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info_kwargs(n1=1, n2=2, n3=3, n4=4, n5=5)
info_kwargs(user="hello", password="world")
'''
<class 'dict'> {'n1': 1, 'n2': 2, 'n3': 3, 'n4': 4, 'n5': 5}
n1: 1
n2: 2
n3: 3
n4: 4
n5: 5
<class 'dict'> {'user': 'hello', 'password': 'world'}
user: hello
password: world
'''