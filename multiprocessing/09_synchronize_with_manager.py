#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 09_synchronize_with_manager.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 09_synchronize_with_manager.py
"""
import multiprocessing

def worker(dictionary, key, item):
    dictionary[key] = item
    print ("key = %s value = %s" %(key, item))

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    dictionary = mgr.dict()
    jobs = [ multiprocessing.Process(target=worker, args=(dictionary, i, i*2)) for i in range(10) ]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print ("Results:", dictionary)
'''
key = 1 value = 2
key = 0 value = 0
key = 2 value = 4
key = 3 value = 6
key = 4 value = 8
key = 5 value = 10
key = 7 value = 14
key = 8 value = 16
key = 9 value = 18
key = 6 value = 12
Results: {1: 2, 0: 0, 2: 4, 3: 6, 4: 8, 5: 10, 7: 14, 8: 16, 9: 18, 6: 12}
'''