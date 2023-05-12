#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 04_subprocess_run_output.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 04_subprocess_run_output.py
"""
import subprocess

completed = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
print('returncode:', completed.returncode)
print('Have {} bytes in stdout:\n{}'.format(len(completed.stdout), completed.stdout.decode('utf-8')))
'''
returncode: 0
Have 440 bytes in stdout:
total 48
-rw-r--r--  1 kang-air  staff  1017  5 12 14:08 01_subprocess_os_system.py
-rw-r--r--  1 kang-air  staff   580  5 12 14:16 02_subprocess_shell_variables.py
-rw-r--r--  1 kang-air  staff   556  5 12 14:22 03_subprocess_run_check.py
-rw-r--r--  1 kang-air  staff   579  5 12 14:28 04_subprocess_run_output.py
-rw-r--r--  1 kang-air  staff   697  5 12 13:42 repeater.py
-rw-r--r--  1 kang-air  staff  1041  5 12 13:50 signal_child.py
'''