#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 11_multiprocessing_simple.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 11_multiprocessing_simple.py
"""
import multiprocessing

def worker():
    """worker function"""
    print ('Worker')
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
'''
Worker
Worker
Worker
Worker
Worker
'''