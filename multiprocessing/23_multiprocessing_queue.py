#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 23_multiprocessing_queue.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 23_multiprocessing_queue.py
"""
import multiprocessing
import time

class MyFancyClass:

    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print('Doing something fancy in {} for {}!'.format(proc_name, self.name))

def worker(queue):
    print(multiprocessing.current_process().name)
    obj = queue.get()
    obj.do_something()

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    lst = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(queue,))
        lst.append(p)
        p.start()

    time.sleep(3)

    queue.put(MyFancyClass('Fancy Dan-1'))
    queue.put(MyFancyClass('Fancy Dan-2'))
    queue.put(MyFancyClass('Fancy Dan-3'))

    # Wait for the worker to finish
    queue.close()
    # queue.join_thread()
    # for p in lst:
    #     p.join()
    time.sleep(3)
'''
Process-1
Doing something fancy in Process-1 for Fancy Dan!
'''