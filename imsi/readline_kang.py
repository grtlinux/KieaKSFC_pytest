#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: readline_kang.py
"""

# ##################################

_fileName = None
_lines = None
_idx = -1
_size = 0

def openFile(fileName):
    ''' open file '''
    global _fileName, _lines, _idx, _size
    _fileName = fileName
    f = open(_fileName, mode='r', encoding='utf-8')
    _lines = f.readlines()
    f.close()
    _size = len(_lines)
    _idx = 0
    pass

def getIdx():
    ''' get index of line in the file '''
    global _lines, _idx, _size
    return _idx

def incIdx():
    global _lines, _idx, _size
    _idx += 1
    pass

def incIdx(idx):
    global _lines, _idx, _size
    _idx += idx
    pass

def setIdx(idx):
    ''' set index to the idx of the file'''
    global _lines, _idx, _size
    _idx = idx
    pass

def printInfo():
    ''' get the information of the file '''
    print('INFO >>> file: {}, rowCnt: {}, currIdx: {}, currLine: {!r}'.format(_fileName, _size, _idx, _lines[_idx].rstrip()))
    pass

def readLine(inc):
    ''' get the line of the file by idx '''
    global _lines, _idx, _size
    if _size <= _idx:
        return None
    line = _lines[_idx].rstrip()
    _idx += inc
    return line

# ##################################

fileName = 'layout.txt'

def process():
    ''' process function '''
    openFile(fileName)

    setIdx(603)
    printInfo()

    print('>>> {} : {}'.format(getIdx(), readLine(1)))
    print('>>> {} : {}'.format(getIdx(), readLine(1)))
    print('>>> {} : {}'.format(getIdx(), readLine(1)))
    print('>>> {} : {}'.format(getIdx(), readLine(1)))
    
    setIdx(500)
    print('>>> {} : {}'.format(getIdx(), readLine(1)))
    print('>>> {} : {}'.format(getIdx(), readLine(1)))
    print('>>> {} : {}'.format(getIdx(), readLine(1)))
    print('>>> {} : {}'.format(getIdx(), readLine(1)))

    if readLine(1) == None:
        print('--- None ---')
    
    pass

if __name__ == '__main__':
    process()
