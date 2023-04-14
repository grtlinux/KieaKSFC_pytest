#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: strip_01.py
"""

TEXT = '  Hello, world!    '

print('{!r}'.format(TEXT.strip()))
print('{!r}'.format(TEXT.lstrip()))
print('{!r}'.format(TEXT.rstrip()))

