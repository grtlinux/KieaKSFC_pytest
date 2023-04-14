#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: layout_06_data.py
"""

import json
import decimal

FILE_NAME = 'layout.txt'
JSON_FILE_NAME = 'layout_data.json'

_DATA = {}
_SCODE = None
_BRES_FLAG = False
# _idxFld = None
_SARR_NAME = None

def makeTitle(line):
    ''' make title from line '''
    '''
    global _data, _sCode
    print()
    # print('>>>', line)
    _sCode = line.split(' ', 1)[1].split('-')[1]
    print('>>> {!r}'.format(_sCode))
    '''
    pass

def makeMethod(line):
    ''' make method from line '''
    pass

def makeReqFlag(line):
    ''' make req flag from line '''
    pass

def makeResFlag(line):
    ''' make res flag from line '''
    '''
    global _data, _bResFlag
    # print('>>>', line)
    _data.clear()
    _bResFlag = True
    '''
    pass

def makeField(line):
    ''' make value field from line '''
    '''
    global _data, _sCode, _bResFlag, _sArrName
    if _bResFlag:
        # print('>>>', line)
        arr = [ a.strip() for a in line.split(':') ]
        # print('>>>', len(arr), arr)
        if '<object>' in line:
            _sArrName = arr[0]
            _data[_sArrName] = []
            _dic.clear()
        else:
            _data[arr[0]] = arr[3]
    '''
    pass

_DIC = {}

def makeArrayField(line):
    ''' make array value field from line '''
    '''
    return
    global _data, _sCode, _bResFlag, _sArrName
    # print('>>>', 'ARR', line)
    arr = [ a.strip() for a in line.split(':')]
    print('>>>', 'ARR', len(arr), arr)
    '''
    '''
    dic = {}
    if ' N(' in line:
        dic[arr[0]] = arr[3]
        # dic[arr[0]] = decimal.Decimal(arr[3])
    else:
        dic[arr[0]] = arr[3]
        # dic[arr[0]] = str(arr[3])
    # _data[_sArrName].append(dic)
    _data[_sArrName][arr[0]] = arr[3]
    _dic[arr[0]] = arr[3]
    '''
    pass





def printJson():
    ''' print the json '''
    global _BRES_FLAG
    print('JSON >>>', json.dumps(_DATA, ensure_ascii=False, indent=2))
    _BRES_FLAG = True
    pass

def saveJsonFile():
    ''' save the json to a file '''
    with open(JSON_FILE_NAME, 'w', encoding='utf-8') as f:
        f.write(json.dumps(_DATA, ensure_ascii=False, indent=2))
    f.close()
    pass



# ##################################

_fileName = 'layout.txt'
_lines = None
_idx = -1
_size = 0

def openFile(fileNama):
    global _lines, _idx, _size
    f = open(FILE_NAME, mode='r', encoding='utf-8')
    _lines = f.readlines()
    f.close()
    _size = len(_lines)
    _idx = 0
    pass

def currIdx():
    global _lines, _idx, _size
    return _idx

def setIdx(idx):
    global _lines, _idx, _size
    _idx = idx
    pass

def printInfo():
    print('INFO >>> ', _idx, _size, _lines[_idx].rstrip())
    pass

def readLine(inc):
    global _lines, _idx, _size
    if _size <= _idx:
        return None
    line = _lines[_idx].rstrip()
    _idx += inc
    return line

# ##################################


def process():
    ''' process function '''
    openFile(_fileName)

    printInfo()
    print('>>> {} : {}'.format(currIdx(), readLine(603)))
    print('>>> {} : {}'.format(currIdx(), readLine(1)))
    print('>>> {} : {}'.format(currIdx(), readLine(1)))
    print('>>> {} : {}'.format(currIdx(), readLine(1)))
    
    setIdx(500)
    print('>>> {} : {}'.format(currIdx(), readLine(1)))
    print('>>> {} : {}'.format(currIdx(), readLine(1)))
    print('>>> {} : {}'.format(currIdx(), readLine(1)))
    print('>>> {} : {}'.format(currIdx(), readLine(1)))

    if readLine(1) == None:
        print('--- None ---')
    
    pass

if __name__ == '__main__':
    process()



