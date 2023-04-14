#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
# end_pymotw_header
# file: .pylintrc

"""
program:  dict_contains_02.py
"""

tag_dict = {'파이썬':0,'코딩':0,'자바':0,'프로그램':0,'Python':0}

def input_dict(tag_name:str):
    ''' input_dict '''
    if tag_name in tag_dict:
        tag_dict[tag_name] += 1
    else:
        tag_dict[tag_name] = 1


input_dict('임시')
input_dict('Python')
input_dict('자바')
input_dict('자바')
input_dict('자바')
input_dict('파이썬')
input_dict('파이썬')

print(tag_dict)
