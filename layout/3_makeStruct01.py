# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: 3_makeStruct01.py
'''
program: 3_makeStruct01.py
comment:
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
def get_struct(lst: list=None, indent: str='') -> list:
  ''' get_struct '''
  lstSt = list()
  for itm in lst:
    if itm['type'] == 'ARROBJ':
      lstSt.append('%sstruct {' % (indent))
      indent2 = indent + '   '
      lstSt.extend(get_struct(lst=itm['arrFields'], indent=indent2))
      lstSt.append('%s} %-30s [%3d];' % (indent, itm['fieldName'], itm['arrMax']))
    else:
      lstSt.append('%schar %-30s [%3d];' % (indent, itm['fieldName'], itm['size']))
  return lstSt

# ----------------------------------------------
def get_reqres_struct(file_name) -> None:
  ''' get_reqres_struct '''
  print(getFuncName(), file_name)
  with open(file_name, mode='r', encoding='utf8') as f:
    dic = json.load(f)
  f.close()

  if 'struct' in dic: del dic['struct']
  # if 'struct' in dic: dic.pop('struct')

  lstReq = list()
  lstReq.append('typedef struct {')
  lstReq.extend(get_struct(lst=dic['reqFields'], indent='    '))
  lstReq.append('} STRUCT_000_REQ;')
  lstRes = list()
  lstRes.append('typedef struct {')
  lstRes.extend(get_struct(lst=dic['resFields'], indent='    '))
  lstRes.append('} STRUCT_000_RES;')

  struct_dic = dict()
  struct_dic['req'] = lstReq
  struct_dic['res'] = lstRes
  dic['struct'] = struct_dic
  # print('>>>', json.dumps(struct_dic, ensure_ascii=False, indent=4))

  with open(file_name, mode='w', encoding='utf8') as f:
    json.dump(dic, f, ensure_ascii=False, indent=2)
  f.close()

# ----------------------------------------------
def get_trx_struct(file_path, lst_files) -> None:
  ''' get_trx_struct '''
  for file in lst_files:
    file_name = '/'.join([file_path, file])
    get_reqres_struct(file_name)

# ----------------------------------------------
TRX_PATH = '/content/drive/MyDrive/json'

if __name__ == '__main__':
  # get_reqres_struct('/content/drive/MyDrive/json/trx_001.json')
  lst_files = get_trx_list(TRX_PATH)
  get_trx_struct(TRX_PATH, lst_files)
