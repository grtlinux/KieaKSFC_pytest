#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 25_multiprocessing_producer_consumer.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 25_multiprocessing_producer_consumer.py
"""
import multiprocessing
import time

class Consumer(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Poison pill means shutdown
                print('{}: Exiting'.format(proc_name))
                self.task_queue.task_done()
                break
            time.sleep(0.1)
            print('{}: {}'.format(proc_name, next_task))
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)
        return

class Task:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        time.sleep(0.1)  # pretend to take time to do the work
        return '{self.a} * {self.b} = {product}'.format(self=self, product=self.a * self.b)

    def __str__(self):
        return '{self.a} * {self.b}'.format(self=self)

if __name__ == '__main__':
    # Establish communication queues
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    # Start consumers
    num_consumers = multiprocessing.cpu_count()
    print('Creating {} consumers'.format(num_consumers))
    consumers = [Consumer(tasks, results) for i in range(num_consumers)]
    for w in consumers:
        w.start()

    # Enqueue jobs
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i, i))

    # Add a poison pill for each consumer
    for i in range(num_consumers):
        tasks.put(None)

    # Wait for all of the tasks to finish
    tasks.join()

    # Start printing results
    while num_jobs:
        result = results.get()
        print('Result:', result)
        num_jobs -= 1
'''
Creating 4 consumers
Consumer-1: 0 * 0
Consumer-3: 1 * 1
Consumer-4: 2 * 2
Consumer-2: 3 * 3
Consumer-1: 4 * 4
Consumer-3: 5 * 5
Consumer-4: 7 * 7
Consumer-2: 6 * 6
Consumer-4: Exiting
Consumer-2: Exiting
Consumer-1: 8 * 8
Consumer-3: 9 * 9
Consumer-1: Exiting
Consumer-3: Exiting
Result: 0 * 0 = 0
Result: 1 * 1 = 1
Result: 2 * 2 = 4
Result: 3 * 3 = 9
Result: 4 * 4 = 16
Result: 5 * 5 = 25
Result: 7 * 7 = 49
Result: 6 * 6 = 36
Result: 8 * 8 = 64
Result: 9 * 9 = 81
'''