#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
#
#
"""
program: layout_05_data.py
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
    global _DATA, _SCODE
    print()
    # print('>>>', line)
    _SCODE = line.split(' ', 1)[1].split('-')[1]
    print('>>> {!r}'.format(_SCODE))
    pass

def makeMethod(line):
    ''' make method from line '''
    pass

def makeReqFlag(line):
    ''' make req flag from line '''
    pass

def makeResFlag(line):
    ''' make res flag from line '''
    global _DATA, _BRES_FLAG
    # print('>>>', line)
    _DATA.clear()
    _BRES_FLAG = True
    pass

def makeField(line):
    ''' make value field from line '''
    global _DATA, _SCODE, _BRES_FLAG, _SARR_NAME
    if _BRES_FLAG:
        # print('>>>', line)
        arr = [ a.strip() for a in line.split(':') ]
        # print('>>>', len(arr), arr)
        if '<object>' in line:
            _SARR_NAME = arr[0]
            _DATA[_SARR_NAME] = []
            _DIC.clear()
        else:
            _DATA[arr[0]] = arr[3]
    pass

_DIC = {}

def makeArrayField(line):
    ''' make array value field from line '''
    return
    global _DATA, _SCODE, _BRES_FLAG, _SARR_NAME
    # print('>>>', 'ARR', line)
    arr = [ a.strip() for a in line.split(':')]
    print('>>>', 'ARR', len(arr), arr)
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
    '''
    _DIC[arr[0]] = arr[3]
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

def readline():
    with open(FILE_NAME, mode='r', encoding='utf-8') as f:
        for line in f:
            if line.strip() == '': continue
            line = line.rstrip()
            # print('3>>>', line)

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
                # saveJsonFile()
            else:
                pass
    f.close()
    pass

if __name__ == '__main__':
    readline()



