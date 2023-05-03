#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
'''
program: 03_threading_names.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 03_threading_names.py
'''
import threading
import time

def worker():
    print(threading.current_thread().name, 'Starting')
    time.sleep(0.2)
    print(threading.current_thread().name, 'Exiting')

def my_service():
    print(threading.current_thread().name, 'Starting')
    time.sleep(3)
    print(threading.current_thread().name, 'Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()
'''
worker Starting
Thread-1 (worker) Starting
my_service Starting
worker Exiting
Thread-1 (worker) Exiting
my_service Exiting
'''
