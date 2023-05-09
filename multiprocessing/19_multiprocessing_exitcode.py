#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 19_multiprocessing_exitcode.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 19_multiprocessing_exitcode.py
"""
import multiprocessing
import time
import sys

def exit_error():
    sys.exit(1)

def exit_ok():
    return

def return_value():
    return 1

def raises():
    raise RuntimeError('There was an error!')

def terminated():
    time.sleep(3)

if __name__ == '__main__':
    jobs = []
    funcs = [exit_error, exit_ok, return_value, raises, terminated]
    for f in funcs:
        print('Starting process for', f.__name__)
        j = multiprocessing.Process(target=f, name=f.__name__)
        jobs.append(j)
        j.start()

    jobs[-1].terminate()

    for j in jobs:
        j.join()
        print('{:>15}.exitcode = {}'.format(j.name, j.exitcode))
'''
Starting process for exit_error
Starting process for exit_ok
Starting process for return_value
Starting process for raises
Starting process for terminated
     exit_error.exitcode = 1
        exit_ok.exitcode = 0
   return_value.exitcode = 0
Process raises:
Traceback (most recent call last):
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/kang-air/KANG/_GIT_HUB/python/github/KieaKSFC_pytest/multiprocessing/19_multiprocessing_exitcode.py", line 32, in raises
    raise RuntimeError('There was an error!')
RuntimeError: There was an error!
         raises.exitcode = 1
     terminated.exitcode = -9
'''