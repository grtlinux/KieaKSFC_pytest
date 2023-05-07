#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 01_spawn_a_process.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 01_spawn_a_process.py
"""
import multiprocessing
import time

def function(i):
    print('called function in process: %s START' % i)
    time.sleep(2)
    print('called function in process: %s FINISH' % i)
    return

if __name__ == '__main__':
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=function, args=(i,))
        Process_jobs.append(p)
        p.start()
        # p.join()
'''
called function in process: 0 START
called function in process: 0 FINISH
called function in process: 1 START
called function in process: 1 FINISH
called function in process: 2 START
called function in process: 2 FINISH
called function in process: 3 START
called function in process: 3 FINISH
called function in process: 4 START
called function in process: 4 FINISH

called function in process: 0 START
called function in process: 1 START
called function in process: 2 START
called function in process: 4 START
called function in process: 3 START
called function in process: 0 FINISH
called function in process: 1 FINISH
called function in process: 2 FINISH
called function in process: 4 FINISH
called function in process: 3 FINISH
'''