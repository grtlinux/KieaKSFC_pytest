#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 01_subprocess_os_system.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 01_subprocess_os_system.py
"""
import subprocess

# completed = subprocess.run(['ls', '-l'])
# completed = subprocess.run(['ls', '-l'], capture_output=True)
# completed = subprocess.run(['ls', '-l'], capture_output=True, text=True)
completed = subprocess.run('find ~/KANG -name "*.html" | xargs grep "python"', shell=True)
# print(completed)
# print(completed)
print(completed.stdout)
print('returncode:', completed.returncode)
'''
total 24
-rw-r--r--  1 kang-air  staff   468  5 12 13:55 01_subprocess_os_system.py
-rw-r--r--  1 kang-air  staff   697  5 12 13:42 repeater.py
-rw-r--r--  1 kang-air  staff  1041  5 12 13:50 signal_child.py
CompletedProcess(args=['ls', '-l'], returncode=0)
returncode: 0
'''