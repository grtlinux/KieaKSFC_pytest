#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: 3_makeStruct01.py
'''
program: 3_makeStruct01.py
comment:
    - struct : req / res
    $ python 3_makeStruct01.py
'''
import os
import sys
import sys
import json

# ----------------------------------------------
def getFuncName() -> str:
    ''' getFuncName '''
    return sys._getframe(1).f_code.co_name + ':'

# ----------------------------------------------
def get_trx_list(file_path: str=None) -> list[str]:
    ''' get_trx_list '''
    lst_files = os.listdir(file_path)
    lst_files = [file for file in lst_files if file.startswith('trx_') and file.endswith('.json')]
    lst_files = sorted(lst_files)
    # for file in lst_files: print(file)
    return lst_files

# ----------------------------------------------
def get_struct(lstFlds: list|None= None, indent: str|None= '') -> list:
    ''' get_struct '''
    lstStruct = list()
    indent += '    '
    for fld in lstFlds:
        if fld['type'] == 'ARROBJ':
            lstStruct.append('%sstruct {' % (indent))
            lstStruct.extend(get_struct(lstFlds=fld['arrFields'], indent=indent))
            lstStruct.append('%s}    %-40s [%4d];' % (indent, fld['fieldName'], fld['arrMax']))
        else:
            lstStruct.append('%schar %-40s [%4d];' % (indent, fld['fieldName'], fld['size']))
    return lstStruct

# ----------------------------------------------
def get_reqres_struct(file_name: str|None= None) -> None:
    ''' get_reqres_struct '''
    print(getFuncName(), file_name)
    with open(file_name, mode='r', encoding='utf8') as f:
        dic = json.load(f)
    f.close()

    # del if exist yet
    if 'struct' in dic: del dic['struct']
    # if 'struct' in dic: dic.pop('struct')

    # get the code name
    code = dic['code']
    
    lstReq = list()
    lstReq.append(f'typedef struct {{')
    lstReq.extend(get_struct(lstFlds=dic['reqFields'], indent=''))
    lstReq.append(f'}} STRUCT_{code}_REQ;')
    lstRes = list()
    lstRes.append(f'typedef struct {{')
    lstRes.extend(get_struct(lstFlds=dic['resFields'], indent=''))
    lstRes.append(f'}} STRUCT_{code}_RES;')

    struct_dic = dict()
    struct_dic['req'] = lstReq
    struct_dic['res'] = lstRes
    dic['struct'] = struct_dic
    # print('>>>', json.dumps(struct_dic, ensure_ascii=False, indent=4))

    with open(file_name, mode='w', encoding='utf8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=4)
    f.close()

# ----------------------------------------------
def get_trx_struct(file_path, lst_files) -> None:
    ''' get_trx_struct '''
    for file in lst_files:
        file_name = '/'.join([file_path, file])
        get_reqres_struct(file_name)

# ----------------------------------------------
TRX_PATH = '../json'

if __name__ == '__main__':
    # get_reqres_struct('../json/trx_001.json')
    lst_files = get_trx_list(TRX_PATH)
    get_trx_struct(TRX_PATH, lst_files)
'''
'''