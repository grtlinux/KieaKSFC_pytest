#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 02_naming_a_process.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 02_naming_a_process.py
"""
import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print("Starting %s" % name)
    time.sleep(3)
    print("Exiting %s" % name)

if __name__ == '__main__':
    process_with_name = multiprocessing.Process(name='foo_process', target=foo)
    process_with_default_name = multiprocessing.Process(target=foo)
    process_with_name.start()
    process_with_default_name.start()
'''
Starting Process-2
Starting foo_process
Exiting Process-2
Exiting foo_process
'''