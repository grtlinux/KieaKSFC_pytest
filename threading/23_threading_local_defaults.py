#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
'''
program: 23_threading_local_defaults.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 23_threading_local_defaults.py
'''
import random
import threading
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)

def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)

class MyLocal(threading.local):
    def __init__(self, value):
        super().__init__()
        logging.debug('Initializing %r', self)
        self.value = value

local_data = MyLocal(1000)
show_value(local_data)

for i in range(2):
    t = threading.Thread(
        target=worker,
        args=(local_data,),
    )
    t.start()
'''
(MainThread) Initializing <__main__.MyLocal object at 0x102fcc580>
(MainThread) value=1000
(Thread-1 (worker)) Initializing <__main__.MyLocal object at 0x102fcc580>
(Thread-1 (worker)) value=1000
(Thread-1 (worker)) value=3
(Thread-2 (worker)) Initializing <__main__.MyLocal object at 0x102fcc580>
(Thread-2 (worker)) value=1000
(Thread-2 (worker)) value=20
'''