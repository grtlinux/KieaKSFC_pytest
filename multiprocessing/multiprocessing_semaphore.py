#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: multiprocessing_semaphore.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python multiprocessing_semaphore.py
"""
import random
import multiprocessing
import time

class ActivePool:

    def __init__(self):
        super(ActivePool, self).__init__()
        self.mgr = multiprocessing.Manager()
        self.active = self.mgr.list()
        self.lock = multiprocessing.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)

    def __str__(self):
        with self.lock:
            return str(self.active)

def worker(s, pool):
    name = multiprocessing.current_process().name
    with s:
        pool.makeActive(name)
        print('Activating {} now running {}'.format(name, pool))
        time.sleep(random.random())
        pool.makeInactive(name)

if __name__ == '__main__':
    pool = ActivePool()
    s = multiprocessing.Semaphore(3)
    jobs = [multiprocessing.Process(target=worker, name=str(i), args=(s, pool),) for i in range(10)]

    for j in jobs:
        j.start()

    while True:
        alive = 0
        for j in jobs:
            if j.is_alive():
                alive += 1
                j.join(timeout=0.1)
                print('Now running {}'.format(pool))
        if alive == 0:
            # all done
            break
'''
Traceback (most recent call last):
  File "/Users/kang-air/KANG/_GIT_HUB/python/github/KieaKSFC_pytest/multiprocessing/multiprocessing_semaphore.py", line 56, in <module>
    j.start()
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
TypeError: cannot pickle 'weakref.ReferenceType' object
'''