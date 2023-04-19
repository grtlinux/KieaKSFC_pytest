#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: copyright_props.py
'''
program: copyright_props.py
comment:
    - using find_files.py
    $ python -V
        Python 3.10.9
    $ python copyright_props.py
'''
import os

# ------------------------------------------------------------
HOME_PATH = '/Users/kang-air'
JOB_PATH = os.sep.join([HOME_PATH, 'KANG/_GIT_HUB/python/github', 'KieaKSFC_pytest/copyright'])
BASE_PATH = f'{JOB_PATH}/before'
TO_PATH = f'{JOB_PATH}/after'

# ------------------------------------------------------------
def find_files(path: str, ext: str) -> list:
    ''' find_files '''
    lstFiles = list()
    for root, dirs, files in os.walk(path):
        print('>>>', root, dirs, files)
        for file in files:
            if file.endswith(f".{ext}"):
                lstFiles.append(os.path.join(root, file))
    return lstFiles

# ------------------------------------------------------------
def main() -> None:
    ''' main function '''
    files = find_files(BASE_PATH, 'properties')
    print('>>>', files)
    pass
'''
'''
# ------------------------------------------------------------
if __name__ == '__main__':
    main()
'''
'''