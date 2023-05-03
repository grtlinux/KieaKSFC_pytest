#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
'''
program: 12_threading_event.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 12_threading_event.py
'''
import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

def wait_for_event(e):
    ''' Wait for the event to be set before doing anything '''
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)
    return

def wait_for_event_timeout(e, t):
    ''' Wait t seconds and then timeout '''
    while not e.is_set():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')

e = threading.Event()
t1 = threading.Thread(
    name='blocking',
    target=wait_for_event,
    args=(e,),
)
t1.start()

t2 = threading.Thread(
    name='non-blocking',
    target=wait_for_event_timeout,
    args=(e, 2),
)
t2.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(3)
e.set()
logging.debug('Event is set')
'''
(blocking  ) wait_for_event starting
(non-blocking) wait_for_event_timeout starting
(MainThread) Waiting before calling Event.set()
(non-blocking) event set: False
(non-blocking) doing other work
(non-blocking) wait_for_event_timeout starting
(MainThread) Event is set
(non-blocking) event set: True
(blocking  ) event set: True
(non-blocking) processing event
'''
