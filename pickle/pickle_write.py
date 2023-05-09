#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: pickle_write.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python pickle_write.py
"""
import pickle

my_list = ['this', 'is', 'my', 'list']

with open('my_data.pickle', 'wb') as f:
    pickle.dump(my_list, f)
'''
'''
