#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: path01.py
'''
program: path01.py
comment:
    $ python path01.py
'''
import os

def getPath1():
    ''' getPath1() '''
    print('1>', os.path.abspath(__file__))
    print('1>', os.path.dirname(os.path.abspath(__file__)))
    print('1>', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print()

def getPath2():
    ''' getPath2() '''
    print('2>', os.getcwd())
    print('2>', os.path.dirname(os.getcwd()))
    print('2>', os.path.dirname(os.path.dirname(os.getcwd())))
    print()

def getPath3():
    ''' getPath3() '''
    current_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(current_folder)
    working_dir = os.getcwd()
    print('3>', working_dir)
    print()

def getPath4():
    ''' getPath4() '''
    current_folder = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(current_folder, 'data_org')
    file_path = os.path.join(data_folder, 'text.txt')
    print('4>', file_path)
    print()

def getPath5():
    ''' getPath5() '''
    lst = __file__.split(os.sep)
    lst.reverse()
    print('5>', type(lst), lst)
    print('5>', lst[0])
    pass

def getPath6():
    ''' getPath6() '''
    lst = __file__.split(os.sep)
    print('6>', type(reversed(lst)), [x for x in reversed(lst)][0])
    print('6>', lst[::-1][0])
    pass

if __name__ == '__main__':
    if True: getPath1()
    if True: getPath2()
    if True: getPath3()
    if True: getPath4()
    if True: getPath5()
    if True: getPath6()
    pass