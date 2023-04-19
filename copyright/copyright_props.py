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

import os

# ------------------------------------------------------------
HOME_PATH = '/Users/kang-air'
JOB_PATH = os.sep.join([HOME_PATH, 'KANG/_GIT_HUB/python/github/KieaKSFC_pytest', 'copyright'])
FROM_PATH = f'{JOB_PATH}/before'
TO_PATH = f'{JOB_PATH}/after'

EXT = 'properties'
EXT2 = 'props'

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
'''
'''
# ------------------------------------------------------------
def get_copyright_str(path: str, ext: str) -> str:
    ''' get_copyright_str '''
    with open(f'{path}/copyright_{ext}.txt', 'r') as f:
        return f.read()
    return ''
'''
'''
# ------------------------------------------------------------
def save_copyright_files(files: list, copyright_str: str, to_path: str) -> None:
    ''' save_copyright_files '''
    for file in files:
        to_file = f'{to_path}/{file.split(os.sep)[-1]}'
        with open(file, 'r') as f:
            lines = f.readlines()
        with open(to_file, 'w') as f:
            f.write(copyright_str)
            f.write('\n')
            f.writelines(lines)
'''
'''
# ------------------------------------------------------------
def main() -> None:
    ''' main function '''
    files = find_files(FROM_PATH, EXT)
    copyright_str = get_copyright_str(JOB_PATH, EXT2)
    print('>>>', copyright_str)
    save_copyright_files(files, copyright_str, TO_PATH)
    pass
'''
'''
# ------------------------------------------------------------
if __name__ == '__main__':
    main()
'''
'''