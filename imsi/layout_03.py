#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
"""
program: layout_03.py
"""

import json

DATA = {}

FILE_NAME = 'text.txt'
JSON_FILE_NAME = 'text.json'

def makeTitle(line):
    ''' make title from line '''
    # print('>>>', line)
    arr = line.split(' ', 1)
    arr = arr[1].split('-')
    print()
    # print('>>>', arr)
    DATA.clear()
    DATA['code'] = arr[1]
    DATA['name'] = arr[0]
    # print('data >>>', data)
    # print('json >>>', json.dumps(data, ensure_ascii=False, indent=2))

def makeMethod(line):
    ''' make method from line '''
    # print('>>>', line)
    arr = line.split(' : ')
    # print('>>>', arr)
    DATA['method'] = arr[0]
    DATA['url'] = arr[1]
    # print('data >>>', data)
    # print('json >>>', json.dumps(data, ensure_ascii=False, indent=2))
    
FLAG = None
def makeReqResFlag(line):
    ''' make req/res flag from lineb'''
    global FLAG
    # print('>>>', line)
    if FLAG != line[0:3]:
        FLAG = line[0:3]
        DATA[FLAG.lower() + 'Fields'] = []
    # print('>>> {!r}'.format(flag))
    # print('json >>>', json.dumps(data, ensure_ascii=False, indent=2))

flagInArr = False

def makeField(line):
    ''' make value field from line '''
    global arrObject
    # print('>>>', flag, line)
    arr = [ a.strip() for a in line.split(':') ]
    # print('>>>', flag, len(arr), arr)
    if '<object>' in arr[2]:
        dic = {}
        dic['fieldName'] = arr[0]
        dic['desc'] = arr[1]
        # dic['arrFields'] = []
        # data[flag.lower() + 'Fields'].append(dic)
        arrObject = []
        pass
    elif flagInArr:
        # dic['arrFields'] = []
        DATA[FLAG.lower() + 'Fields'].append(arrObject)
        flagInArr = False

        dic = {}
        dic['fieldName'] = arr[0]
        dic['desc'] = arr[1]
        DATA[FLAG.lower() + 'Fields'].append(dic)
        pass
    else:
        dic = {}
        dic['fieldName'] = arr[0]
        dic['desc'] = arr[1]
        DATA[FLAG.lower() + 'Fields'].append(dic)

arrObject = None
def makeArrayField(line):
    ''' make array value field from line '''
    global flagInArr, arrObject
    flagInArr = True
    # print('>>>', flag, 'ARR', line)
    arr = [ a.strip() for a in line.split(':')]
    # print('>>>', flag, 'ARR', len(arr), arr)
    dic = {}
    dic['fieldName'] = arr[0]
    dic['desc'] = arr[1]
    arrObject.append(dic)

def printJson():
    ''' print the json '''
    print('json >>>', json.dumps(DATA, ensure_ascii=False, indent=2))

def saveJsonFile():
    ''' save the json to a file '''
    with open(JSON_FILE_NAME, 'w', encoding='utf-8') as f:
        f.write(json.dumps(DATA, ensure_ascii=False, indent=2))
    f.close()
    
def readline03():
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
            elif line.startswith('REQ') or line.startswith('RES'):
                makeReqResFlag(line)
                pass
            elif line.startswith('        '):
                #makeArrayField(line)
                pass
            elif line.startswith('    '):
                makeField(line)
                pass
            elif line.startswith('JSON'):
                printJson()
                pass
            else:
                pass
    f.close()


if __name__ == '__main__':
    readline03()
