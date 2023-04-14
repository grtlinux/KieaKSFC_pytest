#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: string_contains_01.py
"""

TEXT = '가나다라 마바사아 자차카타 파하'

print('마바' in TEXT)
print('마바마' in TEXT)
print('마바마' not in TEXT)