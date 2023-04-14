#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: layout_05_info.py
"""

import json

FILE_NAME = 'layout.txt'
JSON_FILE_NAME = 'layout.json'

_DATA = {}
_SGUBUN = None
_IDX_FLD = None
_SARR_FLD = None

def makeTitle(line):
    ''' make title from line '''
    global _DATA
    print()
    # print('>>>', line)
    arr = line.split(' ', 1)
    arr = arr[1].split('-')
    # print('>>>', arr)
    _DATA.clear()
    _DATA['code'] = arr[1]
    _DATA['desc'] = arr[0]
    # print('data >>>', _data)

def makeMethod(line):
    ''' make method from line '''
    global _DATA
    # print('>>>', line)
    arr = line.split(' : ')
    # print('>>>', arr)
    _DATA['method'] = arr[0]
    _DATA['url'] = arr[1]
    # print('data >>>', _data)

def makeReqFlag(line):
    ''' make req flag from line '''
    global _DATA, _SGUBUN, _IDX_FLD
    # print('>>>', line)
    _SGUBUN = line[0:3].lower() + 'Fields'
    _DATA[_SGUBUN] = []
    _IDX_FLD = -1
    # print('>>> {!r}'.format(_sGubun))

def makeResFlag(line):
    ''' make res flag from line '''
    global _DATA, _SGUBUN, _IDX_FLD
    # print('>>>', line)
    _SGUBUN = line[0:3].lower() + 'Fields'
    _DATA[_SGUBUN] = []
    _IDX_FLD = -1
    # print('>>> {!r}'.format(_sGubun))

def makeField(line):
    ''' make value field from line '''
    global _DATA, _SGUBUN, _IDX_FLD, _SARR_FLD
    # print('>>>', line)
    arr = [ a.strip() for a in line.split(':') ]
    # print('>>>', len(arr), arr)
    dic = {}
    dic['fieldName'] = arr[0]
    dic['desc'] = arr[1]
    if ' N(' in line:
        dic['type'] = 'number'
    else:
        dic['type'] = 'string'

    if '<object>' in line:
        dic['arrFields'] = []
    _DATA[_SGUBUN].append(dic)
    _IDX_FLD += 1

def makeArrayField(line):
    ''' make array value field from line '''
    global _DATA, _SGUBUN, _IDX_FLD, _SARR_FLD
    # print('>>>', 'ARR', line)
    arr = [ a.strip() for a in line.split(':')]
    # print('>>>', 'ARR', len(arr), arr)
    dic = {}
    dic['fieldName'] = arr[0]
    dic['desc'] = arr[1]
    if ' N(' in line:
        dic['type'] = 'number'
    else:
        dic['type'] = 'string'
    _DATA[_SGUBUN][_IDX_FLD]['arrFields'].append(dic)

def printJson():
    ''' print the json '''
    print('json >>>', json.dumps(_DATA, ensure_ascii=False, indent=2))

def saveJsonFile():
    ''' save the json to a file '''
    with open(JSON_FILE_NAME, 'w', encoding='utf-8') as f:
        f.write(json.dumps(_DATA, ensure_ascii=False, indent=2))
    f.close()

def readline():
    with open(FILE_NAME, mode='r', encoding='utf-8') as f:
        for line in f:
            if line.strip() == '': continue
            line = line.rstrip()
            # print('3>>>', line)

            if line.startswith('#'):
                makeTitle(line)
                pass
            elif line.startswith('GET') or line.startswith('POST'):
                makeMethod(line)
                pass
            elif line.startswith('REQ'):
                makeReqFlag(line)
                pass
            elif line.startswith('RES'):
                makeResFlag(line)
                pass
            elif line.startswith('        '):
                makeArrayField(line)
                pass
            elif line.startswith('    '):
                makeField(line)
                pass
            elif line.startswith('JSON'):
                printJson()
                saveJsonFile()
                pass
            else:
                pass
    f.close()
    pass


if __name__ == '__main__':
    readline()



