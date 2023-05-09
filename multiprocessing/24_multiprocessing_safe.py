#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 24_multiprocessing_safe.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 24_multiprocessing_safe.py
"""
import multiprocessing
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')

def worker(num, d):
    ''' thread worker function '''
    print('Worker:', num)
    d['a'] = 'b'
    logging.debug(d)

d = {}
d['a'] = 'a'
d['b'] = 'b'
logging.debug(d)

if __name__ == '__main__':
    jobs = []
    for i in range(2):
        p = multiprocessing.Process(target=worker, args=(i, d))
        jobs.append(p)
        p.start()

time.sleep(1)
logging.debug(d)
'''
MainProcess: {'a': 'a', 'b': 'b'}
Process-1: {'a': 'a', 'b': 'b'}
Process-2: {'a': 'a', 'b': 'b'}
MainProcess: {'a': 'a', 'b': 'b'}
Process-1: {'a': 'a', 'b': 'b'}
Worker: 0
Process-1: {'a': 'b', 'b': 'b'}
Process-2: {'a': 'a', 'b': 'b'}
Worker: 1
Process-2: {'a': 'b', 'b': 'b'}
'''