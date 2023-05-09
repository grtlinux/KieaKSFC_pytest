#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 08_process_barrier.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 08_process_barrier.py
"""
import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print(f"process {name} ----> {datetime.fromtimestamp(now)}")

def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print(f"process {name} ----> {datetime.fromtimestamp(now)}")

if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p3 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier', target=test_without_barrier).start()
'''
process p4 - test_without_barrier ----> 2023-05-09 10:01:46.459325
process p3 - test_without_barrier ----> 2023-05-09 10:01:46.460030

Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/spawn.py", line 116, in spawn_main
    exitcode = _main(fd, parent_sentinel)
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/spawn.py", line 126, in _main
    self = reduction.pickle.load(from_parent)
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/synchronize.py", line 110, in __setstate__
    self._semlock = _multiprocessing.SemLock._rebuild(*state)
FileNotFoundError: [Errno 2] No such file or directory

Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/spawn.py", line 116, in spawn_main
    exitcode = _main(fd, parent_sentinel)
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/spawn.py", line 126, in _main
    self = reduction.pickle.load(from_parent)
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/multiprocessing/synchronize.py", line 110, in __setstate__
    self._semlock = _multiprocessing.SemLock._rebuild(*state)
FileNotFoundError: [Errno 2] No such file or directory
'''