#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 18_multiprocessing_terminate.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 18_multiprocessing_terminate.py
"""
import multiprocessing
import time

def slow_worker():
    print('Starting worker')
    time.sleep(0.1)
    print('Finished worker')

if __name__ == '__main__':
    p = multiprocessing.Process(target=slow_worker)
    print('BEFORE:', p, p.is_alive())

    p.start()
    print('DURING:', p, p.is_alive())

    p.terminate()
    print('TERMINATED:', p, p.is_alive())

    p.join()
    print('JOINED:', p, p.is_alive())
'''
BEFORE: <Process name='Process-1' parent=48494 initial> False
DURING: <Process name='Process-1' pid=48521 parent=48494 started> True
TERMINATED: <Process name='Process-1' pid=48521 parent=48494 started> True
JOINED: <Process name='Process-1' pid=48521 parent=48494 stopped exitcode=-SIGTERM> False
'''