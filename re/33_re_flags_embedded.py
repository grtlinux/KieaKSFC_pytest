#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 33_re_flags_embedded.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 33_re_flags_embedded.py
"""
import re

text = 'This is some text -- with punctuation.'
pattern = r'(?i)\bT\w+'
regex = re.compile(pattern)

print('Text:', text)
print('Pattern:', pattern)
print('Matches:', regex.findall(text))
'''
Text: This is some text -- with punctuation.
Pattern: (?i)\bT\w+
Matches: ['This', 'text']
'''