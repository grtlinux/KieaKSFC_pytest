#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: layout_07_info.py
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
    ''' increase index to the idx of the file '''
    global _lines, _idx, _size
    _idx += 1
    pass

def incIdx(idx):
    ''' increase index to the idx of the file '''
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



import json
import re

fileName = 'layout.txt'
jsonFileName = 'trx_{}.json'

_data = {}
_sCode = None
_sGubun = None
_sArrName = None

# ##################################
def makeTitle(line):
    ''' make title from line '''
    global _data, _sCode
    print()
    # print('>>>', line)
    arr = line.split(' ', 1)[1].split('-')
    _sCode = arr[1]
    # print('>>> {!r}'.format(_sCode))
    _data.clear()
    _data['code'] = arr[1]
    _data['desc'] = arr[0]
    # print('data >>>', _data)

def makeMethod(line):
    ''' make method from line '''
    global _data
    # print('>>>', line)
    arr = line.split(' : ')
    # print('>>>', arr)
    _data['method'] = arr[0]
    _data['url'] = arr[1]
    # print('data >>>', _data)

def makeReqFlag(line):
    ''' make req flag from line '''
    global _data, _sGubun, _idxFld
    # print('>>>', line)
    _sGubun = line[0:3].lower() + 'Fields'
    _data[_sGubun] = []
    # print('>>> {!r}'.format(_sGubun))

def makeResFlag(line):
    ''' make res flag from line '''
    global _data, _sGubun, _idxFld
    # print('>>>', line)
    _sGubun = line[0:3].lower() + 'Fields'
    _data[_sGubun] = []
    #_idxFld = -1
    # print('>>> {!r}'.format(_sGubun))

def makeField(line):
    ''' make value field from line '''
    global _data, _sCode, _sGubun, _sArrName
    # print('>>>', line)
    arr = [ a.strip() for a in line.split(':') ]
    # print('>>>', len(arr), arr)

    dic = {}
    dic['fieldName'] = arr[0]
    dic['desc'] = arr[1]
    dic['size'] = int(re.search('[0-9]+', line).group(0))
    if ' N(' in line:
        if '_cnt' in arr[0]:
            dic['type'] = 'ARRCOUNT'
            # dic['arrMax'] = 123
        elif ',' in line:
            dic['type'] = 'DOUBLE'
            dic['precision'] = int(re.search('([0-9]+),([0-9]+)', line).group(2))
        else:
            dic['type'] = 'LONG'
    else:
        dic['type'] = 'STRING'
    
    # array
    if '<object>' in line:
        # arrMax be gotten with re
        del dic['size']
        # srch = re.search('[0-9]+', line)
        # _data[_sGubun][len(_data[_sGubun])-1]['arrMax'] = int(srch.group(0))
        # print('arrMax >>>', srch.group(0), len(_data[_sGubun]))
        dic['arrMax'] = int(re.search('[0-9]+', line).group(0))
        dic['type'] = 'ARROBJECT'
        dic['arrFields'] = []
        while True:
            line = readLine(1)
            if not line.startswith('        '):
                incIdx(-1)
                break

            arr = [ a.strip() for a in line.split(':')]
            dicArr = {}
            dicArr['fieldName'] = arr[0]
            dicArr['desc'] = arr[1]
            dicArr['size'] = int(re.search('[0-9]+', line).group(0))
            if ' N(' in line:
                if '_cnt' in arr[0]:
                    dicArr['type'] = 'ARRCOUNT'
                    # dic['arrMax'] = 123
                elif ',' in line:
                    dicArr['type'] = 'DOUBLE'
                    dicArr['precision'] = int(re.search('([0-9]+),([0-9]+)', line).group(2))
                else:
                    dicArr['type'] = 'LONG'
            else:
                dicArr['type'] = 'STRING'

            dic['arrFields'].append(dicArr)
            pass
    _data[_sGubun].append(dic)
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
            # makeArrayField(line)
            pass
        elif line.startswith('    '):
            makeField(line)
            pass
        elif line.startswith('JSON'):
            printJson()
            saveJsonFile()
        else:
            pass
    pass

if __name__ == '__main__':
    process()



