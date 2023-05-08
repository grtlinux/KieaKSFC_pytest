#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: queue_lifo.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python queue_lifo.py
"""
import queue

queue = queue.LifoQueue()

for i in range(5):
    queue.put(i)

while not queue.empty():
    print(queue.get(), end=' ')
'''
4 3 2 1 0
'''