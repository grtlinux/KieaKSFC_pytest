#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 46_re_split.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 46_re_split.py
"""
import re

text = '''Paragraph one\non two lines.\n\nParagraph two.\n\n\nParagraph three.'''

print('With findall:')
for num, para in enumerate(re.findall(r'(.+?)(\n{2,}|$)', text, flags=re.DOTALL)):
    print(num, repr(para))
    print()

print()
print('With split:')
for num, para in enumerate(re.split(r'\n{2,}', text)):
    print(num, repr(para))
    print()

print(re.findall(r'(.+?)(\n{2,}|$)', text, flags=re.DOTALL))
print(type(re.findall(r'(.+?)(\n{2,}|$)', text, flags=re.DOTALL)))
'''
With findall:
0 ('Paragraph one\non two lines.', '\n\n')

1 ('Paragraph two.', '\n\n\n')

2 ('Paragraph three.', '')


With split:
0 'Paragraph one\non two lines.'

1 'Paragraph two.'

2 'Paragraph three.'

[('Paragraph one\non two lines.', '\n\n'), ('Paragraph two.', '\n\n\n'), ('Paragraph three.', '')]
<class 'list'>
'''