#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
'''
program: 08_threading_enumerate.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 08_threading_enumerate.py
'''
import threading
import time
import logging
import random

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

def worker():
    """thread worker function"""
    pause = random.randint(1, 5) / 10
    logging.debug('sleeping %0.2f', pause)
    time.sleep(pause)
    logging.debug('ending')

for i in range(3):
    t = threading.Thread(target=worker, daemon=True)
    t.start()

main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.name)
    t.join()
'''
(Thread-1 (worker)) sleeping 0.40
(Thread-2 (worker)) sleeping 0.20
(Thread-3 (worker)) sleeping 0.10
(MainThread) joining Thread-1 (worker)
(Thread-3 (worker)) ending
(Thread-2 (worker)) ending
(Thread-1 (worker)) ending
(MainThread) joining Thread-2 (worker)
(MainThread) joining Thread-3 (worker)
'''