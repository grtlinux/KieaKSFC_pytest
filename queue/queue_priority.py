#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: queue_priority.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python queue_priority.py
"""
import functools
import queue
import threading

@functools.total_ordering
class Job:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
        return

    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented

queue = queue.PriorityQueue()

queue.put(Job(3, 'Mid-level job'))
queue.put(Job(10, 'Low-level job'))
queue.put(Job(1, 'Important job'))

def process_job(queue):
    while True:
        next_job = queue.get()
        print('Processing job:', next_job.description)
        queue.task_done()

workers = [
    threading.Thread(target=process_job, args=(queue,)),
    threading.Thread(target=process_job, args=(queue,)),
]

for w in workers:
    w.daemon = True
    w.start()

queue.join()
'''
New job: Mid-level job
New job: Low-level job
New job: Important job
Processing job: Important job
Processing job: Mid-level job
Processing job: Low-level job
'''