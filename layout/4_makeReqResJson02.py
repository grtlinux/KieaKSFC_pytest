#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: 4_makeReqResJson02.py
'''
program: 4_makeReqResJson02.py
comment:
    - make req / res json
    $ python 4_makeReqResJson02.py
'''
import os
import sys
import json

# ----------------------------------------------
FLG_PRINT = False

# ----------------------------------------------
def getFuncName() -> str:
    ''' getFuncName '''
    return sys._getframe(1).f_code.co_name + ':'

# ----------------------------------------------
def get_trx_list(file_path: str|None= None) -> list[str]:
    ''' get_trx_list '''
    lst_files = os.listdir(file_path)
    lst_files = [file for file in lst_files if file.startswith('trx_') and file.endswith('.json')]
    lst_files = sorted(lst_files)
    # for file in lst_files: print(file)
    return lst_files

# ----------------------------------------------
def initJob(jsonFilePath: str|None= None) -> None:
    ''' initJob '''
    print('>>> initJob ...')
    if not os.path.exists(jsonFilePath):
        os.mkdir(jsonFilePath)
        print(f'>>> mkdir({jsonFilePath})')
    else:
        print(f'>>> {jsonFilePath}: exists')
    pass

# ----------------------------------------------
def get_dict(lstFlds: list|None= None) -> dict:
    ''' get_dict '''
    dicRet = dict()
    for fld in lstFlds:
        # arrCnt
        if fld['type'] == 'ARRCNT':
            arrCnt = int(fld['testValue'])

        # if array object
        if fld['type'] == 'ARROBJ':
            dicRet[fld['fieldName']] = [get_dict(fld['arrFields']) for _ in range(arrCnt)]
        else:
            dicRet[fld['fieldName']] = fld['testValue']
        
    return dicRet

# ----------------------------------------------
def readTrxToReqResJson(jsonFilePath: str|None= None) -> None:
    ''' readTrxToReqResJson '''
    for trxFile in get_trx_list(jsonFilePath):
        with open(f'{jsonFilePath}/{trxFile}', mode='r', encoding='utf8') as f:
            dicTrx = json.load(f)
        f.close()

        # trxInfo code
        code = dicTrx['code']

        # make req_XXX.json
        jsonFileName = f'{jsonFilePath}/req_{code}.json'
        dic = get_dict(dicTrx['reqFields'])
        with open(jsonFileName, 'w', encoding='utf8') as file:
            file.write(json.dumps(dic, ensure_ascii=False, indent=4))
        file.close()
        print(getFuncName(), jsonFileName)

        # make res_XXX.json
        jsonFileName = f'{jsonFilePath}/res_{code}.json'
        dic = get_dict(dicTrx['resFields'])
        with open(jsonFileName, 'w', encoding='utf8') as file:
            file.write(json.dumps(dic, ensure_ascii=False, indent=4))
        file.close()
        print(getFuncName(), jsonFileName)
    pass

# ----------------------------------------------
def lastJob():
    ''' lastJob '''
    print('>>> lastJob ...')
    pass

# ----------------------------------------------
FILE_PATH = '..'
JSON_FILE_PATH = f'{FILE_PATH}/json'

# ----------------------------------------------
if __name__ == '__main__':
    initJob(JSON_FILE_PATH)
    readTrxToReqResJson(JSON_FILE_PATH)
    lastJob()
'''
'''