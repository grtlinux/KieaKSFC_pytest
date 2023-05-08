#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 05_subclass_process.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 05_subclass_process.py
"""
import multiprocessing

class MyProcess(multiprocessing.Process):

    def run(self):
        print('called run method in %s' % self.name)
        return
    
if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = MyProcess()
        jobs.append(p)
        p.start()
        p.join()
'''
called run method in MyProcess-1
called run method in MyProcess-2
called run method in MyProcess-3
called run method in MyProcess-4
called run method in MyProcess-5
'''