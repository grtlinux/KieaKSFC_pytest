#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
'''
program: 11_threading_timer.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 11_threading_timer.py
'''
import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

def delayed():
    logging.debug('worker running')
    return

t1 = threading.Timer(0.3, delayed)
t1.name = 't1'
t2 = threading.Timer(0.3, delayed)
t2.name = 't2'

logging.debug('starting timers')
t1.start()
t2.start()

logging.debug('waiting before canceling %s', t2.name)
time.sleep(0.2)
logging.debug('canceling %s', t2.name)
t2.cancel()
logging.debug('done')
'''
'''

