#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 09_subprocess_popen_read.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 09_subprocess_popen_read.py
"""
import subprocess

print('read:')
proc = subprocess.Popen(
    ['echo', '"to stdout"'],
    stdout=subprocess.PIPE,
)
print(proc.communicate())
stdout_value = proc.communicate()[0].decode('utf-8')
print('stdout:', repr(stdout_value))
'''
read:
(b'"to stdout"\n', None)
Traceback (most recent call last):
  File "/Users/kang-air/KANG/_GIT_HUB/python/github/KieaKSFC_pytest/subprocess/09_subprocess_popen_read.py", line 25, in <module>
    stdout_value = proc.communicate()[0].decode('utf-8')
  File "/Users/kang-air/.pyenv/versions/3.10.9/lib/python3.10/subprocess.py", line 1141, in communicate
    stdout = self.stdout.read()
ValueError: read of closed file
'''