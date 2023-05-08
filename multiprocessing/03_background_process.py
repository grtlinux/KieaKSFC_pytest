#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 03_background_process.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 03_background_process.py
"""
import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print("Starting %s" % name)
    time.sleep(3)
    print("Exiting %s" % name)

if __name__ == '__main__':
    background_process = multiprocessing.Process(name='background_process', target=foo)
    background_process.daemon = True

    no_background_process = multiprocessing.Process(name='no_background_process', target=foo, daemon=False)
    # no_background_process.daemon = False

    background_process.start()
    no_background_process.start()
'''
Starting no_background_process
Exiting no_background_process
'''