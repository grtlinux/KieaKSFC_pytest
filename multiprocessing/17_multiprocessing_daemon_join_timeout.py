#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 17_multiprocessing_daemon_join_timeout.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 17_multiprocessing_daemon_join_timeout.py
"""
import multiprocessing
import time
import sys

def daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('Exiting :', p.name, p.pid)
    sys.stdout.flush()

def non_daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    print('Exiting :', p.name, p.pid)
    sys.stdout.flush()

if __name__ == '__main__':
    d = multiprocessing.Process(
        name='daemon',
        target=daemon,
        daemon=True
    )

    n = multiprocessing.Process(
        name='non-daemon',
        target=non_daemon,
        daemon=False
    )

    d.start()
    time.sleep(1)
    n.start()

    d.join(1)
    print('d.is_alive()', d.is_alive())
    n.join()
'''
Starting: daemon 48245
Starting: non-daemon 48246
Exiting : non-daemon 48246
d.is_alive() True
'''