#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: 1_makeTrx01.py
'''
program: 1_makeTrx01.py
comment:
    - 최초 trx_999.json 파일을 만들고, 이후(2,3)에는 trx_999.json 파일을 수정한다.
    $ python 1_makeTrx01.py
'''
import os
import sys
import re
import json

# ----------------------------------------------
FLG_PRINT = False

DATA = dict()
CODE = None
REQRES_NAME = None
ARR_OBJ = None

TYPE_NUM = 'NUMBER'  # right arrage
TYPE_DBL = 'NUMDBL'  # right arrage double/flaot
TYPE_STR = 'STRING'  # left arrage
TYPE_CNT = 'ARRCNT'  # array count
TYPE_OBJ = 'ARROBJ'  # array object <object>

LST_CODE = ['000','999','002','004']
LST_CODE = ['004']
LST_CODE = None

# ----------------------------------------------
def getFuncName() -> str:
  ''' getFuncName '''
  return sys._getframe(1).f_code.co_name + ':'

# ---------------------------------------------- init
def initJob(jsonFilePath: str) -> None:
    ''' initJob '''
    print('>>> initJob...')
    if not os.path.exists(jsonFilePath):
        os.mkdir(jsonFilePath)
        print(f'>>> mkdir({jsonFilePath})')
    else:
      print(f'>>> {jsonFilePath}: exists')
    pass

# ---------------------------------------------- Title
def makeTitle(line: str) -> None:
    ''' makeTitle '''
    global FLG_PRINT, CODE
    # print('title:', line)
    lst = line.split(' ', 1)[1].split('-')[::-1]
    # print('title:', lst)
    if LST_CODE == None or lst[0] in LST_CODE:
        FLG_PRINT = True
        DATA.clear()
        DATA['code'] = lst[0]
        DATA['name'] = lst[1]
        CODE = DATA['code']
    else:
        FLG_PRINT = False
    return

# ---------------------------------------------- Method
def makeMethod(line: str) -> None:
    ''' makeMethod '''
    # print('method:', line)
    if not FLG_PRINT:
        return
    lst = re.split(r'\s*:\s*', line)
    # print('method:', lst)
    DATA['method'] = lst[0]
    DATA['version'] = '/v1'
    DATA['path'] = lst[1]
    pass

# ---------------------------------------------- Req/Res
def makeReqRes(line: str) -> None:
    ''' makeReqRes '''
    global REQRES_NAME
    # print('reqres:', line)
    if not FLG_PRINT:
        return
    REQRES_NAME = re.split(r'\W+', line)[0].lower() + 'Fields'
    DATA[REQRES_NAME] = list()
    pass

# ---------------------------------------------- Array Field
def makeArrayField(line: str) -> None:
    ''' makeArrayField '''
    # print('arrField:', line)
    if not FLG_PRINT:
        return
    lst = re.split(r'\s*:\s*', line.strip(), maxsplit=0, flags=0)
    # print('arrField:', lst)
    dic = dict()
    ARR_OBJ.append(dic)
    # base
    dic['fieldName'] = lst[0]
    dic['desc'] = lst[1]

    # 2023-04-05: json 항목추가
    if len(lst) == 5:
        dic['required'] = lst[2]
        dic['typeInfo'] = lst[3]
        dic['testValue'] = lst[4]
    elif len(lst) == 4:
        dic['required'] = 'Y'
        dic['typeInfo'] = lst[2]
        dic['testValue'] = lst[3]
        
    # size and precision
    size = re.findall(r'\(([\,0-9]+)\)', line)[-1].split(',')
    dic['size'], dic['precision'] = [int(size[i]) if i < len(size) else 0 for i in range(2)]

    # type
    if ' N(' in line:
        if ',' in re.findall(r'\(([\.\,0-9]+)\)', line)[0]:
            dic['type'] = TYPE_DBL    # NUMDBL
        else:
            dic['type'] = TYPE_NUM    # NUMBER
    else:
        dic['type'] = TYPE_STR      # STRING
    pass

# ---------------------------------------------- Field
def makeField(line: str) -> None:
    ''' makeField '''
    global ARR_OBJ
    # print('field:', line)
    if not FLG_PRINT:
        return
    lst = re.split(r'\s*:\s*', line.strip(), maxsplit=0, flags=0)
    # print('field:', lst)
    dic = dict()
    DATA[REQRES_NAME].append(dic)
    # base
    dic['fieldName'] = lst[0]
    dic['desc'] = lst[1]

    # 2023-04-05: json 항목추가
    if len(lst) == 5:
        dic['required'] = lst[2]
        dic['typeInfo'] = lst[3]
        dic['testValue'] = lst[4]
    elif len(lst) == 4 and not '<object>' in line:
        dic['required'] = 'Y'
        dic['typeInfo'] = lst[2]
        dic['testValue'] = lst[3]

    # size and precision
    size = re.findall(r'\(([\,0-9]+)\)', line)[-1].split(',')
    dic['size'], dic['precision'] = [int(size[i]) if i < len(size) else 0 for i in range(2)]

    # type
    if '<object>' in line:
        dic['type'] = TYPE_OBJ      # ARROBJ
        dic['arrMax'] = dic['size']
        del dic['size']
        del dic['precision']
        dic['arrFields'] = list()
        ARR_OBJ = dic['arrFields']
    elif '_cnt' in line:
        dic['type'] = TYPE_CNT      # ARRCNT
    elif ' N(' in line:
        if ',' in re.findall(r'\(([\.\,0-9]+)\)', line)[0]:
            dic['type'] = TYPE_DBL    # NUMDBL
        else:
            dic['type'] = TYPE_NUM    # NUMBER
    else:
        dic['type'] = TYPE_STR      # STRING
    pass

# ---------------------------------------------- Json
def printJson():
    ''' printJson '''
    if not FLG_PRINT:
        return
    print('JSON>>>', json.dumps(DATA, ensure_ascii=False, indent=2))
    pass

# ---------------------------------------------- make Json File
def makeJsonFile(jsonFilePath: str) -> None:
    ''' makeJsonFile '''
    if not FLG_PRINT:
        return
    jsonFileName = f'{jsonFilePath}/trx_{CODE}.json'
    # if os.path.exists(jsonFileName):
    #   os.system(f'rm -rf {jsonFileName}')
    #   print('>>> remove:', jsonFileName)
    
    with open(jsonFileName, 'w', encoding='utf8') as file:
        # ensure_ascii가 True(기본값)이면, 출력에서 모든 비 ASCII 문자가 이스케이프 되도록
        # 보장됩니다. ensure_ascii가 False이면, 그 문자들은 있는 그대로 출력됩니다.
        file.write(json.dumps(DATA, ensure_ascii=False, indent=4))
    file.close()
    
    # print('>>> done', jsonFileName)
    print(getFuncName(), jsonFileName)
    pass

# ---------------------------------------------- Layout To Json
def readLayoutToJson(txtFileName: str, jsonFilePath: str) -> None:
    ''' readLayoutToJson '''
    with open(txtFileName, mode='r', encoding='utf8') as file:
        for line in file:
            line = line.rstrip()
            if line == '' or line.startswith('-'):
                continue
            # print('>>>', line)

            if line.startswith('#'):
                makeTitle(line)
                pass
            elif line.startswith('GET') or line.startswith('POST'):
                makeMethod(line)
                pass
            elif line.startswith('REQ') or line.startswith('RES'):
                makeReqRes(line)
                pass
            elif line.startswith('        '):
                makeArrayField(line)
                pass
            elif line.startswith('    '):
                makeField(line)
                pass
            elif line.startswith('JSON'):
                if DATA['code'] == '999': DATA['version'] = ''
                # printJson()
                makeJsonFile(jsonFilePath)
            pass
    file.close()

# ---------------------------------------------- last
def lastJob():
    ''' lastJob '''
    print('>>> finish...')
    pass

# ----------------------------------------------
FILE_PATH = '..'
TXT_FILE_NAME = f'{FILE_PATH}/data_org/layout.txt'
JSON_FILE_PATH = f'{FILE_PATH}/json'

# ----------------------------------------------
if __name__ == '__main__':
    initJob(JSON_FILE_PATH)
    readLayoutToJson(TXT_FILE_NAME, JSON_FILE_PATH)
    lastJob()
'''
'''