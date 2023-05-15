#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 20_re_groups_individual.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 20_re_groups_individual.py
"""
import re

text = 'This is some text -- with punctuation.'
print("text: {}".format(text))
print("----------------------------------------")

# word starting with t, then another word
regex = re.compile(r'(\bt\w+)\W+(\w+)')
print("regex: {}".format(regex))

match = regex.search(text)
print('Entire match          : ', match.group(0))
print('Word starting with "t": ', match.group(1))
print('Word after "t" word   : ', match.group(2))
print("----------------------------------------")
'''
text: This is some text -- with punctuation.
----------------------------------------
regex: re.compile('(\\bt\\w+)\\W+(\\w+)')
Entire match          :  text -- with
Word starting with "t":  text
Word after "t" word   :  with
----------------------------------------
'''