#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: multiprocessing_pool_maxtasksperchild.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python multiprocessing_pool_maxtasksperchild.py
"""
import multiprocessing

def do_calculation(data):
    return data * 2

def start_process():
    print('Starting', multiprocessing.current_process().name)

if __name__ == '__main__':
    inputs = list(range(10))
    print('Input   :', inputs)

    builtin_outputs = map(do_calculation, inputs)
    print('Built-in:', builtin_outputs)

    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_size, initializer=start_process, maxtasksperchild=2,)
    pool_outputs = pool.map(do_calculation, inputs)
    pool.close()  # no more tasks
    pool.join()  # wrap up current tasks

    print('Pool    :', pool_outputs)
'''
Input   : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Built-in: <map object at 0x10fd93f10>
Starting SpawnPoolWorker-1
Starting SpawnPoolWorker-2
Starting SpawnPoolWorker-3
Starting SpawnPoolWorker-4
Starting SpawnPoolWorker-8
Starting SpawnPoolWorker-7
Starting SpawnPoolWorker-6
Starting SpawnPoolWorker-5
Pool    : [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
'''