#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
'''
program: 13_threading_lock.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 13_threading_lock.py
'''
import threading
import time
import logging
import random

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

class Counter:
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()

def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

logging.debug('Waiting for worker threads')
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Counter: %d', counter.value)

'''
(Thread-1 (worker)) Sleeping 0.78
(Thread-2 (worker)) Sleeping 0.54
(MainThread) Waiting for worker threads
(Thread-2 (worker)) Waiting for lock
(Thread-2 (worker)) Acquired lock
(Thread-2 (worker)) Sleeping 0.42
(Thread-1 (worker)) Waiting for lock
(Thread-1 (worker)) Acquired lock
(Thread-1 (worker)) Sleeping 0.83
(Thread-2 (worker)) Waiting for lock
(Thread-2 (worker)) Acquired lock
(Thread-2 (worker)) Done
(Thread-1 (worker)) Waiting for lock
(Thread-1 (worker)) Acquired lock
(Thread-1 (worker)) Done
(MainThread) Counter: 4
'''
