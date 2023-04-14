#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
"""
program: layout_02.py
"""

FILE_NAME = 'text.txt'

def makeTitle(line):
    ''' make title from line '''
    # print('>>>', line)
    arr = line.split(' ', 1)
    arr = arr[1].split('-')
    print()
    print('>>>', arr)

def makeMethod(line):
    ''' make method from line '''
    # print('>>>', line)
    arr = line.split(' : ')
    print('>>>', arr)

FLAG = None
def makeReqResFlag(line):
    ''' make req/res flag from lineb'''
    global FLAG
    # print('>>>', line)
    if FLAG != line[0:3]:
        FLAG = line[0:3]
    # print('>>> {!r}'.format(flag))

arrName = None
def makeField(line):
    ''' make value field from line '''
    # print('>>>', flag, line)
    arr = [ a.strip() for a in line.split(':') ]
    print('>>>', FLAG, len(arr), arr)

def makeArrayField(line):
    ''' make array value field from line '''
    # print('>>>', flag, 'ARR', line)
    arr = [ a.strip() for a in line.split(':')]
    print('>>>', FLAG, 'ARR', len(arr), arr)

def readline03():
    ''' readLine3() '''
    with open(FILE_NAME, mode='r', encoding='utf-8') as f:
        for line in f:
            if line.strip() == '':
                continue
            line = line.rstrip()
            # print('3>>>', line)
            if line.startswith('#'):
                makeTitle(line)
                pass
            elif line.startswith('GET') or line.startswith('POST'):
                makeMethod(line)
                pass
            elif line.startswith('REQ') or line.startswith('RES'):
                makeReqResFlag(line)
                pass
            elif line.startswith('        '):
                makeArrayField(line)
                pass
            elif line.startswith('    '):
                makeField(line)
                pass
            else:
                pass
    f.close()


if __name__ == '__main__':
    readline03()
