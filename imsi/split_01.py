#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: split_01.py
"""

text = 'fld01:fld02:fld03:fld04:fld05'
strings = text.split(':', 1)

print(strings)


