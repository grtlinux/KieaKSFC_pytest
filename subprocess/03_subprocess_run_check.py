#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 03_subprocess_run_check.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 03_subprocess_run_check.py
"""
import subprocess

try:
    completed = subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as err:
    print("Error:", err)
'''
Error: Command '['false']' returned non-zero exit status 1.
'''