#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
"""
program: layout_01_path.py
"""

import os

def getPath1():
    ''' getPath1() '''
    print('>>>', os.path.abspath(__file__))
    print('>>>', os.path.dirname(os.path.abspath(__file__)))
    print('>>>', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print()

def getPath2():
    ''' getPath2() '''
    print('>>>', os.getcwd())
    print('>>>', os.path.dirname(os.getcwd()))
    print('>>>', os.path.dirname(os.path.dirname(os.getcwd())))
    print()

def getPath3():
    ''' getPath3() '''
    current_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(current_folder)
    working_dir = os.getcwd()
    print('>>>', working_dir)
    print()

def getPath4():
    ''' getPath4() '''
    current_folder = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(current_folder, 'data_org')
    file_path = os.path.join(data_folder, 'text.txt')
    print('>>>', file_path)
    print()


if __name__ == '__main__':
    getPath1()
    getPath2()
    getPath3()
    getPath4()
    pass
