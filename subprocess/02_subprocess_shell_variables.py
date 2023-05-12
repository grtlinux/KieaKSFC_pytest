#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 02_subprocess_shell_variables.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 02_subprocess_shell_variables.py
"""
import subprocess

completed = subprocess.run('echo $HOME', shell=True, text=True, capture_output=True)
print('output:', completed.stdout)
print('returncode:', completed.returncode)
'''
output: /Users/kang-air
returncode: 0
'''