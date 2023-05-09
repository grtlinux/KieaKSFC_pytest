#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 14_multiprocessing_names.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 14_multiprocessing_names.py
"""
import multiprocessing
import time

def worker():
    name = multiprocessing.current_process().name
    print(name, 'Starting')
    time.sleep(2)
    print(name, 'Exiting')

def my_service():
    name = multiprocessing.current_process().name
    print(name, 'Starting')
    time.sleep(3)
    print(name, 'Exiting')

if __name__ == '__main__':
    service = multiprocessing.Process(name='my_service', target=my_service)
    worker_1 = multiprocessing.Process(name='worker 1', target=worker)
    worker_2 = multiprocessing.Process(target=worker) # use default name

    worker_1.start()
    worker_2.start()
    service.start()
'''
worker 1 Starting
Process-3 Starting
my_service Starting
worker 1 Exiting
Process-3 Exiting
my_service Exiting
'''