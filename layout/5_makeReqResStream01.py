#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: 5_makeReqResStream01.py
'''
program: 5_makeReqResStream01.py
comment:
    - make req / res stream
    $ python 5_makeReqResStream01.py
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
def get_stream(lstFlds: list|None= None, flgBlank: bool|None= False) -> list:
    ''' get_stream '''
    lstStream = list()
    for fld in lstFlds:
        # arrCnt
        if fld['type'] == 'ARRCNT':
            arrCnt = int(fld['testValue'])

        # if array object
        if fld['type'] == 'ARROBJ':
            arrMax = int(fld['arrMax'])
            # lstStream.extend([get_stream(fld['arrFields']) if i < arrCnt else get_stream(fld['arrFields'], True)for i in range(arrMax)])
            for i in range(arrMax):
                if i < arrCnt:
                    lstStream.extend(get_stream(fld['arrFields']))
                else:
                    lstStream.extend(get_stream(fld['arrFields'], True))
        elif not flgBlank:
            size = fld['size']
            if fld['type'] == 'STRING':
                # lstStream.append(f"[%-{fld['size']}s]" % (fld['testValue']))
                # lstStream.append(f"%-{fld['size']}s" % (fld['testValue']))
                lstStream.append(f"{fld['testValue']: <{size}}")
            else:
                # lstStream.append(f"[%{fld['size']}s]" % (fld['testValue']))
                # lstStream.append(f"%{fld['size']}s" % (fld['testValue']))
                lstStream.append(f"{fld['testValue']: >{size}}")
        else:
            lstStream.append(' ' * fld['size'])
        
    return lstStream

# ----------------------------------------------
def readTrxToReqResStream(jsonFilePath: str|None= None) -> None:
    ''' readTrxToReqResStream '''
    for trxFile in get_trx_list(jsonFilePath):
        with open(f'{jsonFilePath}/{trxFile}', mode='r', encoding='utf8') as f:
            dicTrx = json.load(f)
        f.close()

        # trxInfo code
        code = dicTrx['code']
    
        # make req_XXX.json
        jsonFileName = f'{jsonFilePath}/sreq_{code}.txt'
        lstStream = get_stream(dicTrx['reqFields'])
        # print('>>>', jsonFileName, lstStream)
        # sys.exit()
        with open(jsonFileName, 'w', encoding='euckr') as file:
            file.write(''.join(lstStream))
        file.close()
        print(getFuncName(), jsonFileName)

        # make res_XXX.json
        jsonFileName = f'{jsonFilePath}/sres_{code}.txt'
        lstStream = get_stream(dicTrx['resFields'])
        with open(jsonFileName, 'w', encoding='euckr') as file:
            file.write(''.join(lstStream))
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
    readTrxToReqResStream(JSON_FILE_PATH)
    lastJob()
'''
'''