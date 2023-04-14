# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: 4_makeReqResJson01.py
'''
program: 4_makeReqResJson01.py
comment:
    $ python 4_makeReqResJson01.py
'''
import os
import re
import json

# ----------------------------------------------
FLG_PRINT = False

CODE = None
DATA = None
REQ_DATA = None
RES_DATA = None
REQ_NAME = None
RES_NAME = None

JSON_NAME = None

ARR_CNT = None
ARR_OBJ = None

LST_CODE = ['000','999','002','004']
LST_CODE = ['004']
LST_CODE = ['001']
LST_CODE = None

# ----------------------------------------------
def initJob(jsonFilePath):
  ''' initJob '''
  print('>>> initJob ...')
  if not os.path.exists(jsonFilePath):
    os.mkdir(jsonFilePath)
    print(f'>>> mkdir({jsonFilePath})')
  else:
    print(f'>>> {jsonFilePath}: exists')
  pass

# ----------------------------------------------
def makeTitle(line, jsonFilePath):
  ''' makeTitle '''
  global FLG_PRINT, CODE
  # print('title:', line)
  lst = line.split(' ', 1)[1].split('-')[::-1]
  if LST_CODE == None or lst[0] in LST_CODE:
    # print('title:', lst)
    FLG_PRINT = True
    CODE = lst[0]
    JSON_NAME
  else:
    FLG_PRINT = False
    return
  pass

# ----------------------------------------------
def makeMethod(line):
  ''' makeMethod (NOT_USED) '''
  pass

# ----------------------------------------------
def makeReq(line):
  ''' makeReqRes '''
  global REQ_NAME, REQ_DATA, DATA
  # print('req:', line)
  if FLG_PRINT:
    # print('req:', line)
    DATA = dict()
    REQ_NAME = ''.join([re.split(r'\W+', line)[0].lower(), '_', CODE, '.json'])
    REQ_DATA = DATA
  pass

# ----------------------------------------------
def makeRes(line):
  ''' makeReqRes '''
  global RES_NAME, RES_DATA, DATA
  # print('res:', line)
  if FLG_PRINT:
    # print('res:', line)
    DATA = dict()
    RES_NAME = ''.join([re.split(r'\W+', line)[0].lower(), '_', CODE, '.json'])
    RES_DATA = DATA
  pass

# ----------------------------------------------
def makeArrayField(line):
  ''' makeArrayField '''
  global ARR_OBJ
  # print('arrField:', line)
  if FLG_PRINT:
    lst = re.split(r'\s*:\s*', line.strip(), maxsplit=0, flags=0)
    # print('arrField:', lst)
    for i in range(ARR_CNT):
      ARR_OBJ[i][lst[0]] = lst[-1]
  pass

# ----------------------------------------------
def makeField(line):
  ''' makeField '''
  global ARR_OBJ, ARR_CNT, DATA
  # print('field:', line)
  if  FLG_PRINT:
    lst = re.split(r'\s*:\s*', line.strip(), maxsplit=0, flags=0)
    # print('field:', lst)
    if '<object>' in line:
      ARR_CNT = int(DATA[list(DATA.keys())[-1]])    # ARR_OBJ 항목의 이전 _cnt 정보 얻는다.
      # ARR_OBJ = list({} for i in range(ARR_CNT))
      ARR_OBJ = list({'__id__':i} for i in range(ARR_CNT))

      if not False:
        # __arrMax
        arrMax = re.findall(r'\(([0-9]+)\)', line)[0]
        DATA['__arrMax__' + lst[0]] = arrMax

      DATA[lst[0]] = ARR_OBJ
    else:
      DATA[lst[0]] = lst[-1]
  pass

# ----------------------------------------------
def printJson():
  ''' printJson '''
  if FLG_PRINT:
    print('REQ_JSON>>>', json.dumps(REQ_DATA, ensure_ascii=False, indent=2))
    print('RES_JSON>>>', json.dumps(RES_DATA, ensure_ascii=False, indent=2))
  pass

# ----------------------------------------------
def makeJsonFile(jsonFilePath):
  ''' makeJsonFile '''
  global REQ_NAME, REQ_DATA, RES_NAME, RES_DATA
  if FLG_PRINT:
    # make req_XXX.json
    jsonFileName = ''.join([jsonFilePath, '/', REQ_NAME])
    with open(jsonFileName, 'w', encoding='utf8') as file:
      file.write(json.dumps(REQ_DATA, ensure_ascii=False, indent=2))
    file.close()
    print('>>>', jsonFileName)

    # make res_XXX.json
    jsonFileName = ''.join([jsonFilePath, '/', RES_NAME])
    with open(jsonFileName, 'w', encoding='utf8') as file:
      file.write(json.dumps(RES_DATA, ensure_ascii=False, indent=2))
    file.close()
    print('>>>', jsonFileName)

  pass

# ----------------------------------------------
def readLayoutToReqResJson(txtFileName, jsonFilePath):
  ''' readLayoutToReqResJson '''
  with open(txtFileName, mode='r', encoding='utf8') as file:
    for line in file:
      line = line.rstrip()
      if line == '':
        continue
      # print('>>> ', line)
      if line.startswith('#'):
        makeTitle(line, jsonFilePath)
        pass
      elif line.startswith('GET') or line.startswith('POST'):
        # makeMethod(line)
        pass
      elif line.startswith('REQ'):
        makeReq(line)
        pass
      elif line.startswith('RES'):
        makeRes(line)
        pass
      elif line.startswith('        '):
        makeArrayField(line)
        pass
      elif line.startswith('    '):
        makeField(line)
        pass
      elif line.startswith('JSON'):
        # printJson()
        makeJsonFile(jsonFilePath)
        pass
  file.close()

# ----------------------------------------------
def lastJob():
  ''' lastJob '''
  print('>>> lastJob ...')
  pass

# ----------------------------------------------
FILE_PATH = '/content/drive/MyDrive'
JSON_FILE_PATH = f'{FILE_PATH}/json'
TXT_FILE_NAME = f'{FILE_PATH}/layout.txt'

# ----------------------------------------------
if __name__ == '__main__':
  initJob(JSON_FILE_PATH)
  readLayoutToReqResJson(TXT_FILE_NAME, JSON_FILE_PATH)
  lastJob()
