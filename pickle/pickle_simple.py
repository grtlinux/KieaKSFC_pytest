#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: pickle_simple.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python pickle_simple.py
"""
users = {'kim':'3kid9', 'sun80':'393948', 'ljm':'py90390'}
f = open('users', 'wb')
import pickle
pickle.dump(users, f)
f.close()

import os
os.path.exists('users')

f = open('users', 'rb')
a = pickle.load(f)
print(a)
'''
{'kim':'3kid9', 'sun80':'393948', 'ljm':'py90390'}
'''