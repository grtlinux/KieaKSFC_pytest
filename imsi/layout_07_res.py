#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: layout_07_res.py
"""

# --- package start --------------------------

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

# --- package end --------------------------

import json
from decimal import Decimal

fileName = 'layout.txt'
jsonFileName = 'res_{}.json'

_data = {}
_sCode = None

_bResFlag = False
_sArrName = None

# ##################################
def makeTitle(line):
    ''' make title from line '''
    global _data, _sCode
    print()
    # print('>>>', line)
    _sCode = line.split(' ', 1)[1].split('-')[1]
    print('>>> {!r}'.format(_sCode))
    # pass

def makeMethod(line):
    ''' make method from line '''
    pass

def makeReqFlag(line):
    ''' make req flag from line '''
    pass

def makeResFlag(line):
    ''' make res flag from line '''
    global _data, _bResFlag
    # print('>>>', line)
    _data.clear()
    _bResFlag = True
    pass

def makeField(line):
    ''' make value field from line '''
    global _data, _sCode, _bResFlag, _sArrName
    if _bResFlag:
        # print('>>>', line)
        arr = [ a.strip() for a in line.split(':') ]
        # print('>>>', len(arr), arr)
        if '<object>' in line:
            _sArrName = arr[0]
            _data[_sArrName] = []

            dic = {}
            # print('>>>', _sArrName)
            while True:
                line = readLine(1)
                if not line.startswith('        '):
                    incIdx(-1)
                    break
                arr = [ a.strip() for a in line.split(':')]
                # print('>>>', 'ARR', len(arr), arr)
                # dic[arr[0]] = arr[3]
                if ' N(' in line:
                    try:
                        dic[arr[0]] = int(arr[3])
                    except ValueError:
                        dic[arr[0]] = float(arr[3])
                else:
                    dic[arr[0]] = arr[3]
                pass
            _data[_sArrName].append(dic)
        else:
            if ' N(' in line:
                try:
                    _data[arr[0]] = int(arr[3])
                except ValueError:
                    _data[arr[0]] = float(arr[3])
            else:
                _data[arr[0]] = arr[3]
    pass

def makeArrayField(line):
    ''' make array value field from line '''
    '''
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





# ##################################
def printJson():
    ''' print the json '''
    global _bResFlag
    print('JSON >>>', json.dumps(_data, ensure_ascii=False, indent=2))
    _bResFlag = False
    pass

def saveJsonFile():
    ''' save the json to a file '''
    with open(jsonFileName.format(_sCode), 'w', encoding='utf-8') as f:
        f.write(json.dumps(_data, ensure_ascii=False, indent=2))
    f.close()
    pass


# ##################################
def process():
    ''' process function '''
    openFile(fileName)
    printInfo()

    while True:
        line = readLine(1)
        if line == None: break
        if line.strip() == '': continue

        if line.startswith('#'):
            makeTitle(line)
        elif line.startswith('GET') or line.startswith('POST'):
            makeMethod(line)
        elif line.startswith('REQ'):
            makeReqFlag(line)
        elif line.startswith('RES'):
            makeResFlag(line)
        elif line.startswith('        '):
            makeArrayField(line)
        elif line.startswith('    '):
            makeField(line)
        elif line.startswith('JSON'):
            printJson()
            saveJsonFile()
        else:
            pass
    pass


if __name__ == '__main__':
    process()
    '''
    str = '1234.12'
    print('>>> ', type(str), str)
    num = Decimal(str)
    print('>>> ', type(num), num)
    pass
    '''

    '''
    str = '{"name":"hello"}'
    jsonStr = json.loads(str)
    print(jsonStr, type(jsonStr))
    '''
    pass

