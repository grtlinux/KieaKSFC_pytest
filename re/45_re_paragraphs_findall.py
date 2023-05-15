#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 45_re_paragraphs_findall.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 45_re_paragraphs_findall.py
"""
import re

text = '''Paragraph one\non two lines.\n\nParagraph two.\n\n\nParagraph three.'''

for num, para in enumerate(re.findall(r'(.+?)\n{2,}', text, flags=re.DOTALL)):
    print(num, repr(para))
    print()

print(re.findall(r'(.+?)\n{2,}', text, flags=re.DOTALL))
print(type(re.findall(r'(.+?)\n{2,}', text, flags=re.DOTALL)))

print(re.findall(r'(.+?)(\n{2,})', text, flags=re.DOTALL))

print(re.findall(r'.+?\n{2,}', text, flags=re.DOTALL))
'''
0 'Paragraph one\non two lines.'

1 'Paragraph two.'

['Paragraph one\non two lines.', 'Paragraph two.']
<class 'list'>
[('Paragraph one\non two lines.', '\n\n'), ('Paragraph two.', '\n\n\n')]
['Paragraph one\non two lines.\n\n', 'Paragraph two.\n\n\n']
'''