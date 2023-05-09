#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 22_multiprocessing_subclass.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 22_multiprocessing_subclass.py
"""
import multiprocessing

class Worker(multiprocessing.Process):
    
    def run(self):
        print('In %s' % self.name)
        return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
'''
In Worker-1
In Worker-3
In Worker-2
In Worker-4
In Worker-5
'''