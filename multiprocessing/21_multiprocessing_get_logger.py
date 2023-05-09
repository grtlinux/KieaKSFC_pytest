#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 21_multiprocessing_get_logger.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 21_multiprocessing_get_logger.py
"""
import multiprocessing
import logging
import sys

def worker():
    print('Doing some work')
    sys.stdout.flush()

if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG)
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
'''
[INFO/Process-1] child process calling self.run()
Doing some work
[INFO/Process-1] process shutting down
[INFO/Process-1] process exiting with exitcode 0
[INFO/MainProcess] process shutting down
'''