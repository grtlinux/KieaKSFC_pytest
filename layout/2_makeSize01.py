#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: 2_makeSize01.py
'''
program: 2_makeSize01.py
comment:
    - length : req / res
    $ python 2_makeSize01.py
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
def get_trx_list(file_path: str|None= None) -> list[str]:
    ''' get_trx_list '''
    lst_files = os.listdir(file_path)
    lst_files = [file for file in lst_files if file.startswith('trx_') and file.endswith('.json')]
    lst_files = sorted(lst_files)
    # for file in lst_files: print(file)
    return lst_files

# ----------------------------------------------
def get_length(lstFlds: list|None= None) -> int:
    ''' get_length '''
    len = 0
    for fld in lstFlds:
        if fld['type'] == 'ARROBJ':
            len += get_length(fld['arrFields']) * fld['arrMax']
        else:
            len += fld['size']
    return len

# ----------------------------------------------
def get_reqres_length(file_name: str|None= None) -> None:
    ''' get_reqres_length '''
    print(getFuncName(), file_name)
    with open(file_name, mode='r', encoding='utf8') as f:
        dic = json.load(f)
    f.close()

    if 'length' in dic: del dic['length']
    # if 'length' in dic: dic.pop('length')

    len_dic = dict()
    len_dic['req'] = get_length(dic['reqFields'])
    len_dic['res'] = get_length(dic['resFields'])
    dic['length'] = len_dic
    # print('>>>', json.dumps(len_dic, ensure_ascii=False, indent=4))

    with open(file_name, mode='w', encoding='utf8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=4)
    f.close()

# ----------------------------------------------
def get_trx_length(file_path, lst_files) -> None:
  ''' get_trx_length '''
  for file in lst_files:
    file_name = '/'.join([file_path, file])
    get_reqres_length(file_name)

# ----------------------------------------------
TRX_PATH = '../json'

if __name__ == '__main__':
    # get_reqres_length('../json/trx_001.json')
    lst_files = get_trx_list(TRX_PATH)
    get_trx_length(TRX_PATH, lst_files)

'''
'''