#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: web01.py
    RUN:
        $ python -V
            Python 3.10.9
        $ pip install fastapi uvicorn
        $ uvicorn web01:app --reload --port=8080 --host=0.0.0.0
"""

from fastapi import FastAPI
import os
import json
import time
from pydantic import BaseModel

app = FastAPI()

# ---------------------------------------------------------------- index
@app.get('/')
async def index():
    '''
    ### index
    ``` shell
        curl -X 'GET' \\
            'http://localhost:8000/' \\
            -H 'accept: application/json'
    ```
    '''
    return {'message': 'Hello, world! (강석) 안녕하세요! こんにちは!'}

# ---------------------------------------------------------------- read_json
JSON_PATH = "../json02"
def read_json(id: int):
    ''' read_json '''
    fileName = '/'.join([JSON_PATH, 'res_%03d.json'%(id)])
    if not os.path.exists(fileName):
        return {'message': 'file not found'}
    with open(fileName, 'r') as f:
        dic = json.load(f)
    f.close()
    return dic

# ---------------------------------------------------------------- 
# ---------------------------------------------------------------- 
# ---------------------------------------------------------------- 
# ---------------------------------------------------------------- GET Samples
"""
@app.get('/get/{id}')
async def getId(id: int) -> dict:
    ''' get : http://localhost:8080/get/2'''
    print('GET: id {}'.format(id))
    return read_json(id)

@app.get('/get2/{id}')
async def getId2(id: int, fld1: str='fld1', fld2: int=123) -> dict:
    ''' get : http://localhost:8080/get2/3?fld1=abc&fld2=123 '''
    print('GET: id {}'.format(id))
    print('GET: fld1={}, fld2={}'.format(fld1, fld2))
    return read_json(id)
"""

# ---------------------------------------------------------------- POST Samples
"""
from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Union
class Image(BaseModel):
    url: HttpUrl
    name: str

class Req2Items(BaseModel):
    code: str = 'CD001'
    description: Optional[str] = None
    price: float = 123.12
    count: int = 123
    tags: Union[List[str], None] = None
    # tags: list[str] | None = None
    images: Union[List[Image], None] = [
    # images: list[Image] | None = [
        {
            'url': 'http://example.org/images',
            'name': 'example.org'
        },{
            'url': 'http://sample.org/images',
            'name': 'sample.org'
        }
    ]
    dumps: Union[List[str], None] = ['홍','강','김']  # list()
    str00s: List[int] = [1,2,3]
    str01s: List[str] = ['1','2','3','4','5','6','7','8']

@app.post('/post')
async def post(req: Req2Items) -> dict:
    ''' post '''
    print('POST-1: req {}'.format(json.dumps(req.dict(), ensure_ascii=False, indent=2)))
    return read_json(2)

# ---------------------------------------------------------------- POST
class Req3Items(BaseModel):
    param1: str = None
    param2: str = None

@app.post('/v1/post')
async def v1Post(req: Req3Items) -> dict:
    ''' post '''
    # print('hello, world!')
    print('POST-2: req {}'.format(json.dumps(req.dict(), ensure_ascii=False, indent=2)))
    # print('POST: req {}'.format(json.dumps(req.dict(), ensure_ascii=False, indent=2)))
    return read_json(3)
"""
# ---------------------------------------------------------------- 
# ---------------------------------------------------------------- 
# ---------------------------------------------------------------- 
# ---------------------------------------------------------------- class RequestHandler
class SettlementInfoWithdraw(BaseModel):
    bank_code: str
    settlement_account_num: str
    settlement_amt: float

class DepositRequirementChangeDetails(BaseModel):
    deposit_requirement_type: str
    increase_amt: float
    decrease_amt: float

class SettlementInfo(BaseModel):
    bank_code: str
    settlement_account_num: str
    settlement_amt: float

class SettlementInfoRffp(BaseModel):
    bank_code: str
    settlement_account_num: str
    settlement_amt: int

class Req004Items(BaseModel):
    account_num: str = 'ABCD1234'
    currency_code: str = 'KRW'
    tran_amt: int = 20000
    withdraw_reason_code: str = 'A1'
    settlement_info_withdraw_cnt: int = 2
    settlement_info_withdraw: list[SettlementInfoWithdraw] | None = [
        {
            'bank_code': 'B1',
            'settlement_account_num': 'BBBB2222',
            'settlement_amt': 300.00
        },{
            'bank_code': 'C1',
            'settlement_account_num': 'DDDD1111',
            'settlement_amt': 200.00
        }
    ]
    consignment_guarantee : float = 123.12
    deposit_requirement_change_details_cnt : int = 123
    deposit_requirement_change_details : list[DepositRequirementChangeDetails] | None = [
        {
            'deposit_requirement_type': 'B2',
            'increase_amt': 123.12,
            'decrease_amt': 123.12
        }, {
            'deposit_requirement_type': 'C2',
            'increase_amt': 111.11,
            'decrease_amt': 111.11
        }
    ]
    optr_email_yn: str = 'Y'
    optr_email_address: str = '4455qqq@naver.com'
    apvr_email_yn: str = 'Y'
    apvr_email_address: str = 'gksruf2848@naver.com'
    optr_sms_yn: str = 'Y'
    optr_mobile_num: int = '01054149634'
    apvr_sms_yn: str = 'Y'
    apvr_mobile_num: int = '01058446024'

class Req005Items(BaseModel):
    account_num: str = 'ABCD1234'
    currency_code: int = 123
    tran_amt: int = 20000
    settlement_info_deposit_cnt: int = 2
    settlement_info_withdraw: list[SettlementInfoWithdraw] | None = [
        {
            'bank_code': 'B1',
            'settlement_account_num': 'BBBB2222',
            'settlement_amt': 300.00
        },{
            'bank_code': 'C1',
            'settlement_account_num': 'DDDD1111',
            'settlement_amt': 200.00
        }
    ]
    consignment_guarantee: float = 123.123
    deposit_requirement_change_details_cnt: int = 123
    deposit_requirement_change_details: list[DepositRequirementChangeDetails] | None = [
        {
            'deposit_requirement_type': 'B2',
            'increase_amt': 123.12,
            'decrease_amt': 123.12
        }, {
            'deposit_requirement_type': 'C2',
            'increase_amt': 111.11,
            'decrease_amt': 111.11
        }
    ]
    optr_email_yn: str = 'Y'
    optr_email_address: str = '4455qqq@naver.com'
    apvr_email_yn: str = 'Y'
    apvr_email_address: str = 'gksruf2848@naver.com'
    optr_sms_yn: str = 'Y'
    optr_mobile_num: int = '01054149634'
    apvr_sms_yn: str = 'Y'
    apvr_mobile_num: int = '01058446024'

class Req006Items(BaseModel):
    code: str = 'CD001' #code
    account_num: str = 'ABCD1234'
    tran_idn_num: str = 'ABC123'

class Req011Items(BaseModel):
    code: str = 'CD001' #code
    account_num: str = 'ABCD1234'
    currency_code: int = 123
    increase_closing_amt: float = 20000.00
    decrease_closing_amt: float = 20000.00
    withdraw_reason: str = 'N1'
    settlement_info_cnt: int = 2
    settlement_info: list[SettlementInfo] | None = [
        {
            'bank_code': 'B1',
            'settlement_account_num': 'BBBB2222',
            'settlement_amt': 300.00
        },{
            'bank_code': 'C1',
            'settlement_account_num': 'DDDD1111',
            'settlement_amt': 200.00
        }
    ]
    consignment_guarantee: float = 123.123
    deposit_requirement_change_details_cnt: int = 123
    deposit_requirement_change_details: list[DepositRequirementChangeDetails] | None = [
        {
            'deposit_requirement_type': 'B2',
            'increase_amt': 123.12,
            'decrease_amt': 123.12
        }, {
            'deposit_requirement_type': 'C2',
            'increase_amt': 111.11,
            'decrease_amt': 111.11
        }
    ]
    optr_email_yn: str = 'Y'
    optr_email_address: str = '4455qqq@naver.com'
    apvr_email_yn: str = 'Y'
    apvr_email_address: str = 'gksruf2848@naver.com'
    optr_sms_yn: str = 'Y'
    optr_mobile_num: int = '01054149634'
    apvr_sms_yn: str = 'Y'
    apvr_mobile_num: int = '01058446024'

class Req012Items(BaseModel):
    code: str = 'CD001' #code
    account_num: str = 'ABCD1234'
    base_date: int = 970328
    increase_closing_amt: float = 20000.00
    decrease_closing_amt: float = 20000.00
    withdraw_reason: str = 'N1'
    settlement_info_cnt: int = 2
    settlement_info: list[SettlementInfo] | None = [
        {
            'bank_code': 'B1',
            'settlement_account_num': 'BBBB2222',
            'settlement_amt': 300.00
        },{
            'bank_code': 'C1',
            'settlement_account_num': 'DDDD1111',
            'settlement_amt': 200.00
        }
    ]
    next_tran_date_rffp_req_amt: int = 20000
    settlement_info_rffp_cnt: int = 2
    settlement_info_rffp: list[SettlementInfoRffp] | None = [
        {
            'bank_code': 'B1',
            'settlement_account_num': 'BBBB2222',
            'settlement_amt': 300.00
        },{
            'bank_code': 'C1',
            'settlement_account_num': 'DDDD1111',
            'settlement_amt': 200.00
        }
    ]
    consignment_guarantee: int = 123
    deposit_requirement_change_details_cnt: int = 2
    deposit_requirement_change_details: list[DepositRequirementChangeDetails] | None = [
        {
            'deposit_requirement_type': 'B2',
            'increase_amt': 123.12,
            'decrease_amt': 123.12
        }, {
            'deposit_requirement_type': 'C2',
            'increase_amt': 111.11,
            'decrease_amt': 111.11
        }
    ]
    optr_email_yn: str = 'Y'
    optr_email_address: str = '4455qqq@naver.com'
    apvr_email_yn: str = 'Y'
    apvr_email_address: str = 'gksruf2848@naver.com'
    optr_sms_yn: str = 'Y'
    optr_mobile_num: int = '01054149634'
    apvr_sms_yn: str = 'Y'
    apvr_mobile_num: int = '01058446024'

class Req013Items(BaseModel):
    code: str = 'CD001' #code
    account_num: str = 'ABCD1234'
    tran_idn_num: str = 'ABC111'

class Req999Items(BaseModel):
    grant_type: str = 'client_credentials'
    client_id: str = '<client_id>'
    client_secret: str = '<client_secret>'
    scope: str = 'manage'

# ---------------------------------------------------------------- 
# ---------------------------------------------------------------- 
# ---------------------------------------------------------------- 
# ----------------------------------------------------------------
VERSION = '/v1' 
# ---------------------------------------------------------------- 
# ---------------------------------------------------------------- GET: 001
# --- 001 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/account_list')
async def get_001_계좌_목록_조회(before_inquiry_trace_info: str) -> dict:
    '''
    # API code : 001
    ## API name : 계좌 목록 조회
    ### API description : 계좌 목록 조회
    #### API method : GET
    ``` shell
    curl -X GET "http://localhost:8080/v1/deposit/invr_dpsa/account_list?before_inquiry_trace_info=1234567890" -H "accept: application/json"
    ```
    '''
    print('REQ >>>', before_inquiry_trace_info)
    return read_json(1)

# ---------------------------------------------------------------- GET: 002
# --- 002 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/account_list_with_balance')
async def get_002_계좌_목록_조회_잔액(dps_mth_dscd: str, before_inquiry_trace_info: int) -> dict:
    ''' get : http://localhost:8080/v1/deposit/invr_dpsa/account_list_with_balance?dps_mth_dscd=1234567890&before_inquiry_trace_info=1234567890 '''
    print('REQ >>>', dps_mth_dscd, before_inquiry_trace_info)
    return read_json(2)

# ---------------------------------------------------------------- GET: 003
# --- 003 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/account/on_demand')
async def get_003_계좌_기본정보_조회_수시입출금(account_num: str, currency_code: int) -> dict:
    ''' get : http://localhost:8080/v1/deposit/invr_dpsa/account/on_demand?account_num=1234567890&currency_code=1234567890 '''
    print('REQ >>>', account_num, currency_code)
    return read_json(3)

# ---------------------------------------------------------------- POST: 004
# --- 004 : POST
@app.post(f'{VERSION}/deposit/invr_dpsa/transfer/withdraw')
async def post_004_수시입출금_신청(reqItems: Req004Items) -> dict:
    '''
    # API code : 004
    ## API name : 수시입출금 신청
    ### API description : 수시입출금 신청
    #### API method : POST
    - $ curl [check](http://localhost:8080/v1/deposit/invr_dpsa/transfer/withdraw)
    '''
    print('REQ >>>', reqItems)
    return read_json(4)

# ---------------------------------------------------------------- POST: 005
# --- 005 : POST
@app.post(f'{VERSION}/deposit/invr_dpsa/transfer/deposit')
async def post_005_마감후입금_신청(reqItems: Req005Items) -> dict:
    '''
    # API code : 005
    ## API name : 마감후입금 신청
    ### API description : 마감후입금 신청
    #### API method : POST
    - [check](http://localhost:8080/v1/deposit/invr_dpsa/transfer/deposit)
    '''
    print('REQ >>>', reqItems)
    return read_json(5)

# ---------------------------------------------------------------- POST: 006
# --- 006 : POST
@app.post(f'{VERSION}/deposit/invr_dpsa/transfer/cancel')
async def post_006_수시입출금_취소(reqItems: Req006Items) -> dict:
    '''
    # API code : 006
    ## API name : 수시입출금 취소
    ### API description : 수시입출금 취소
    #### API method : POST
    - [check](http://localhost:8080/v1/deposit/invr_dpsa/transfer/cancel)
    '''
    print('REQ >>>', reqItems)
    return read_json(6)

# ---------------------------------------------------------------- GET: 007
# --- 007 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/transfer/transaction_list')
async def get_007_수시입출금_신청내역_조회(tran_date: int, search_type: str, prod_code: str, before_inquiry_trace_info: str) -> dict:
    ''' get : http://localhost:8080/v1/deposit/invr_dpsa/transfer/transaction_list?tran_date=20210101&search_type=1&prod_code=1234567890&before_inquiry_trace_info=1234567890 '''
    print('REQ >>>', tran_date, search_type, prod_code, before_inquiry_trace_info)
    return read_json(7)

# ---------------------------------------------------------------- GET: 008
# --- 008 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/transfer/detail')
async def get_008_수시입출금_신청정보_상세조회(account_num: str, tran_date: int, tran_idn_num: str) -> dict:
    ''' get : http://localhost:8080/v1/deposit/invr_dpsa/transfer/detail?account_num=1234567890&tran_date=20210101&tran_idn_num=1234567890 '''
    print('REQ >>>', account_num, tran_date, tran_idn_num)
    return read_json(8)

# ---------------------------------------------------------------- GET: 009
# --- 009 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/account/closing')
async def get_009_계좌_기본정보_조회_마감변동분(tran_date: int, account_num: str, currency_code: str) -> dict:
    ''' get : http://localhost:8080/v1/deposit/invr_dpsa/account/closing?tran_date=20210101&account_num=1234567890&currency_code=1234567890 '''
    print('REQ >>>', tran_date, account_num, currency_code)
    return read_json(9)

# ---------------------------------------------------------------- GET: 010
# --- 010 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/account/closing_and_reserve_for_payment')
async def get_010_계좌_기본정보_조회_마감변동분_지불준비금(tran_date: int, account_num: str) -> dict:
    ''' get : http://localhost:8080/v1/deposit/invr_dpsa/account/closing_and_reserve_for_payment?tran_date=20210101&account_num=1234567890 '''
    print('REQ >>>', tran_date, account_num)
    return read_json(10)

# ---------------------------------------------------------------- POST: 011
# --- 011 : POST
@app.post(f'{VERSION}/deposit/invr_dpsa/transfer/closing')
async def post_011_마감변동분_신청(reqItems: Req011Items) -> dict:
    '''
    # API code : 011
    ## API name : 마감변동분 신청
    ### API description : 마감변동분 신청
    #### API method : POST
    - [check](http://localhost:8080/v1/deposit/invr_dpsa/transfer/closing)
    '''
    print('REQ >>>', reqItems)
    return read_json(11)

# ---------------------------------------------------------------- POST: 012
# --- 012 : POST
@app.post(f'{VERSION}/deposit/invr_dpsa/transfer/closing_and_reserve_for_payment')
async def post_012_마감변동분_신청_지불준비금(reqItems: Req012Items) -> dict:
    '''
    # API code : 012
    ## API name : 마감변동분 신청(지불준비금)
    ### API description : 마감변동분 신청(지불준비금)
    #### API method : POST
    - [check](http://localhost:8080/v1/deposit/invr_dpsa/transfer/closing_and_reserve_for_payment)
    '''
    print('REQ >>>', reqItems)
    return read_json(12)

# ---------------------------------------------------------------- POST: 013
# --- 013 : POST
@app.post(f'{VERSION}/deposit/invr_dpsa/transfer/closing_cancel')
async def post_013_마감변동분_취소(reqItems: Req013Items) -> dict:
    '''
    # API code : 013
    ## API name : 마감변동분 취소
    ### API description : 마감변동분 취소
    #### API method : POST
    - [check](http://localhost:8080/v1/deposit/invr_dpsa/transfer/closing_cancel)
    '''
    print('REQ >>>', reqItems)
    return read_json(13)

# ---------------------------------------------------------------- GET: 014
# --- 014 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/transfer/closing_transaction_list')
async def get_014_마감변동분_신청내역_조회(tran_date: int, dps_mth_dscd: str, prod_code: str, search_type: str, before_inquiry_trace_info: str) -> dict:
    ''' get : http://localhost:8080/v1/deposit/invr_dpsa/transfer/closing_transaction_list?tran_date=20210101&dps_mth_dscd=1&prod_code=1234567890&search_type=1&before_inquiry_trace_info=1234567890 '''
    print('REQ >>>', tran_date, dps_mth_dscd, prod_code, search_type, before_inquiry_trace_info)
    return read_json(14)

# ---------------------------------------------------------------- GET: 015
# --- 015 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/account/transaction_list')
async def get_015_거래내역_조회(account_num: str, currency_code: str, from_date: int, to_date:int, before_inquiry_trace_info: str) -> dict:
    ''' get : http://localhost:8080/v1/deposit/invr_dpsa/account/transaction_list?account_num=1234567890&currency_code=1234567890&from_date=20210101&to_date=20210101&before_inquiry_trace_info=1234567890 '''
    print('REQ >>>', account_num, currency_code, from_date, to_date, before_inquiry_trace_info)
    return read_json(15)

# ---------------------------------------------------------------- GET: 016
# --- 016 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/account/interest_dividend_list')
async def get_016_이자배당내역_조회(account_num: str, currency_code: str, search_year: int) -> dict:
    ''' get : http://localhost:8080/v1/deposit/invr_dpsa/account/interest_dividend_list?account_num=1234567890&currency_code=1234567890&search_year=2021 '''
    print('REQ >>>', account_num, currency_code, search_year)
    return read_json(16)

# ---------------------------------------------------------------- GET: 017
# --- 017 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/account/estimated_interest')
async def get_017_예상이자지급_조회(account_num: str) -> dict:
    ''' get : http://localhost:8080/v1/deposit/invr_dpsa/account/estimated_interest?account_num=1234567890 '''
    print('REQ >>>', account_num)
    return read_json(17)

# ---------------------------------------------------------------- GET: 018
# --- 018 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/account/balance_daily')
async def get_018_일별_잔고_조회(account_num: str, currency_code: str, from_date: int, to_date: int, before_inquiry_trace_info: str) -> dict:
    ''' get : http://localhost:8080/v1/deposit/invr_dpsa/account/balance_daily?account_num=1234567890&currency_code=1234567890&from_date=20210101&to_date=20210101&before_inquiry_trace_info=1234567890 '''
    print('REQ >>>', account_num, currency_code, from_date, to_date, before_inquiry_trace_info)
    return read_json(18)

# ---------------------------------------------------------------- GET: 019
# --- 019 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/account/average_balance_yearly')
async def get_019_평잔_조회_연(account_num: str, currency_code: int, search_year: int) -> dict:
    ''' get : http://localhost:8080/v1/deposit/invr_dpsa/account/average_balance_yearly?account_num=1234567890&currency_code=1234567890&search_year=2021 '''
    print('REQ >>>', account_num, currency_code, search_year)
    return read_json(19)

# ---------------------------------------------------------------- GET: 020
# --- 020 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/account/average_balance_quarterly')
async def get_020_평잔_조회_분기(account_num: str, currency_code: str, search_year: int) -> dict:
    ''' get : http://localhost:8080/v1/deposit/invr_dpsa/account/average_balance_quarterly?account_num=1234567890&currency_code=1234567890&search_year=2021 '''
    print('REQ >>>', account_num, currency_code, search_year)
    return read_json(20)

# ---------------------------------------------------------------- GET: 021
# --- 021 : GET
@app.get(f'{VERSION}/deposit/invr_dpsa/account/average_balance_monthly')
async def get_021_평잔_조회_월(account_num: str, currency_code: str, search_year: int) -> dict:
    ''' get : http://localhost:8080/v1/deposit/invr_dpsa/account/average_balance_monthly?account_num=1234567890&currency_code=1234567890&search_year=2021 '''
    print('REQ >>>', account_num, currency_code, search_year)
    return read_json(21)

# ---------------------------------------------------------------- POST: 999
# --- 999 : POST
@app.post(f'/oauth/2.0/token')
async def post_999_접근토큰_발급(reqItems: Req999Items) -> dict:
    '''
    # API code : 999
    ## API name : 접근토큰 발급
    ### API description : 접근토큰 발급
    #### API method : POST
    ``` shell
        curl -X 'POST' \\
            'http://localhost:8000/oauth/2.0/token' \\
            -H 'accept: application/json' \\
            -H 'Content-Type: application/json' \\
            -d '{
            "grant_type": "client_credentials",
            "client_id": "<client_id>",
            "client_secret": "<client_secret>",
            "scope": "manage"
            }'
    ```
    '''
    print('REQ >>>', reqItems)
    time.sleep(2)  # time(secs) processing for simulation
    return read_json(999)



# ---------------------------------------------------------------- POST
# no used the below
'''
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
'''
