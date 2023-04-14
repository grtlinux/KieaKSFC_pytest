#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
"""
program: layout_01.py
"""

FILE_NAME = 'text.txt'

def readline01():
    ''' readlines() '''
    file = open(FILE_NAME, 'r', encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        if line.strip() == '':
            continue
        line = line.rstrip()
        print('1>>>', line.rstrip())
    file.close()

def readline02():
    ''' readLine2() '''
    f = open(FILE_NAME, 'r', encoding='utf-8')
    for line in f:
        if line.strip() == '':
            continue
        line = line.rstrip()
        print('2>>>', line.rstrip())
    f.close()

def readline03():
    ''' readLine3() '''
    with open(FILE_NAME, mode='r', encoding='utf-8') as f:
        for line in f:
            if line.strip() == '':
                continue
            line = line.rstrip()
            print('3>>>', line)
    f.close()


if __name__ == '__main__':
    #readline01()
    #readline02()
    readline03()
