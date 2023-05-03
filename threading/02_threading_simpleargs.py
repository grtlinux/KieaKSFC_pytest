#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
'''
program: 02_threading_simpleargs.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 02_threading_simpleargs.py
'''

import threading

def worker(num, str):
    """thread worker function"""
    # print('Worker: %s %s' % (num, str))
    print(f'Worker: {num} {str}')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i, 'hello world - ' + str(i)))
    threads.append(t)
    t.start()
'''
Worker: 0
Worker: 1
Worker: 2
Worker: 3
Worker: 4
'''