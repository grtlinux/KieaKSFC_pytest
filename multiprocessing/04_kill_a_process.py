#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 04_kill_a_process.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 04_kill_a_process.py
"""
import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print("Starting function", name)
    time.sleep(10)
    print("Finished function", name)

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print("Process before execution:", p, p.is_alive())

    p.start()
    print("Process running:", p, p.is_alive())

    # p.terminate()
    print("Process terminated:", p, p.is_alive())

    p.join()
    print("Process finished:", p, p.is_alive())

    print("Process exit code:", p.exitcode)
'''
Process before execution: <Process name='Process-1' parent=17052 initial> False
Process running: <Process name='Process-1' pid=17079 parent=17052 started> True
Process terminated: <Process name='Process-1' pid=17079 parent=17052 started> True
Starting function Process-1
Finished function Process-1
Process finished: <Process name='Process-1' pid=17079 parent=17052 stopped exitcode=0> False
Process exit code: 0
'''