#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
# end_pymotw_header
# file: .pylintrc

"""
program: dict_contains_01.py
"""

tag_dict = {'파이썬':0,'코딩':0,'자바':0,'프로그램':0,'Python':0}
TAG_NAME = '임시'

print(tag_dict)


if TAG_NAME in tag_dict:
    tag_dict[TAG_NAME] += 1
else:
    tag_dict[TAG_NAME] = 1

print(tag_dict)
