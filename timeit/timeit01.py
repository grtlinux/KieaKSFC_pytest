#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: path01.py
'''
program: timeit01.py
comment:
    $ python timeit01.py
'''

import timeit

myList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
myList.reverse()
print(myList)

# print(timeit.timeit('"-".join(myList)', setup="from __main__ import myList", number=10000))
print(timeit.timeit('"-".join(reversed(myList))', setup='from __main__ import myList'))
print(timeit.timeit('"-".join(myList[::-1])', setup='from __main__ import myList'))


