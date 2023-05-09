#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 27_multiprocessing_lock.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 27_multiprocessing_lock.py
"""
import multiprocessing
import sys

def worker_with(lock, stream):
    with lock:
        stream.write('Lock acquired via with\n')

def worker_no_with(lock, stream):
    lock.acquire()
    try:
        stream.write('Lock acquired directly\n')
    finally:
        lock.release()

lock = multiprocessing.Lock()
w = multiprocessing.Process(target=worker_with, args=(lock, sys.stdout),)
nw = multiprocessing.Process(target=worker_no_with, args=(lock, sys.stdout),)

w.start()
nw.start()

w.join()
nw.join()
'''
Traceback (most recent call last):
  File "/Users/kang-air/KANG/_GIT_HUB/python/github/KieaKSFC_pytest/multiprocessing/27_multiprocessing_lock.py", line 36, in <module>
    w.start()
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/process.py", line 121, in start
    self._popen = self._Popen(self)
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/context.py", line 224, in _Popen
    return _default_context.get_context().Process._Popen(process_obj)
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/context.py", line 288, in _Popen
    return Popen(process_obj)
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/popen_spawn_posix.py", line 32, in __init__
    super().__init__(process_obj)
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/popen_fork.py", line 19, in __init__
    self._launch(process_obj)
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/popen_spawn_posix.py", line 47, in _launch
    reduction.dump(process_obj, fp)
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/reduction.py", line 60, in dump
    ForkingPickler(file, protocol).dump(obj)
TypeError: cannot pickle '_io.TextIOWrapper' object
'''