#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: layout_07_server3.py
    RUN:
        $ uvicorn layout_07_server:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Set, Union
import json

app = FastAPI()

# --- Req Classes ---
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


# --- getResJson ---
def getResJson(code):
    f = open('res_{}.json'.format(code), mode='r', encoding='utf')
    data = f.read()
    f.close()
    return data


# --- 001 : GET
@app.get('/deposit/invr_dpsa/account_list')
async def getIndex(before_inquiry_trace_info: str):
    print('REQ >>>', before_inquiry_trace_info)
    return json.loads(getResJson('001'))


# --- 002 : GET
@app.get('/deposit/invr_dpsa/account_list_with_balance')
async def getIndex(dps_mth_dscd: str, before_inquiry_trace_info: int):
    print('REQ >>>', dps_mth_dscd, before_inquiry_trace_info)
    return json.loads(getResJson('002'))


# --- 003 : GET
@app.get('/deposit/invr_dpsa/account/on_demand')
async def getIndex(account_num: str, currency_code: int):
    print('REQ >>>', account_num, currency_code)
    return json.loads(getResJson('003'))


# --- 004 : POST
class Req004Items(BaseModel):
    # code: str = 'CD001' #code
    account_num: str = 'ABCD1234'
    currency_code: str = 'KRW'
    tran_amt: int = 20000
    withdraw_reason_code: str = 'A1'
    settlement_info_withdraw_cnt: int = 2
    settlement_info_withdraw: Union[List[SettlementInfoWithdraw], None] = [
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
    deposit_requirement_change_details : Union[List[DepositRequirementChangeDetails], None] = [
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
    

@app.post('/deposit/invr_dpsa/transfer/withdraw')
async def postIndex(reqItems: Req004Items):
    print('REQ >>>', reqItems)
    dic = json.loads(getResJson('004'))
    # dic['rsp_code'] = reqItems.code
    return dic


# --- 005 : POST
class Req005Items(BaseModel):
    code: str = 'CD001' #code
    account_num: str = 'ABCD1234'
    currency_code: int = 123
    tran_amt: int = 20000
    settlement_info_deposit_cnt: int = 2
    settlement_info_withdraw: Union[List[SettlementInfoWithdraw], None] = [
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
    deposit_requirement_change_details: Union[List[DepositRequirementChangeDetails], None] = [
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
    

@app.post('/deposit/invr_dpsa/transfer/deposit')
async def postIndex(reqItems: Req005Items):
    print('REQ >>>', reqItems)
    dic = json.loads(getResJson('005'))
    dic['rsp_code'] = reqItems.code
    return dic


# --- 006 : POST
class Req006Items(BaseModel):
    code: str = 'CD001' #code
    account_num: str = 'ABCD1234'
    tran_idn_num: str = 'ABC123'

@app.post('/deposit/invr_dpsa/transfer/cancel')
async def postIndex(reqItems: Req006Items):
    print('REQ >>>', reqItems)
    dic = json.loads(getResJson('006'))
    dic['rsp_code'] = reqItems.code
    return dic


# --- 007 : GET
@app.get('/deposit/invr_dpsa/transfer/transaction_list')
async def getIndex(tran_date: int, search_type: str, prod_code: str, before_inquiry_trace_info: str):
    print('REQ >>>', tran_date, search_type, prod_code, before_inquiry_trace_info)
    return json.loads(getResJson('007'))


# --- 008 : GET
@app.get('/deposit/invr_dpsa/transfer/detail')
async def getIndex(account_num: str, tran_date: int, tran_idn_num: str):
    print('REQ >>>', account_num, tran_date, tran_idn_num)
    return json.loads(getResJson('008'))


# --- 009 : GET
@app.get('/deposit/invr_dpsa/account/closing')
async def getIndex(tran_date: int, account_num: str, currency_code: str):
    print('REQ >>>', tran_date, account_num, currency_code)
    return json.loads(getResJson('009'))


# --- 010 : GET
@app.get('/deposit/invr_dpsa/account/closing_and_reserve_for_payment')
async def getIndex(tran_date: int, account_num: str):
    print('REQ >>>', tran_date, account_num)
    return json.loads(getResJson('010'))


# --- 011 : POST
class Req011Items(BaseModel):
    code: str = 'CD001' #code
    account_num: str = 'ABCD1234'
    currency_code: int = 123
    increase_closing_amt: float = 20000.00
    decrease_closing_amt: float = 20000.00
    withdraw_reason: str = 'N1'
    settlement_info_cnt: int = 2
    settlement_info: Union[List[SettlementInfo], None] = [
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
    deposit_requirement_change_details: Union[List[DepositRequirementChangeDetails], None] = [
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
    

@app.post('/deposit/invr_dpsa/transfer/closing')
async def postIndex(reqItems: Req011Items):
    print('REQ >>>', reqItems)
    dic = json.loads(getResJson('011'))
    dic['rsp_code'] = reqItems.code
    return dic


# --- 012 : POST
class Req012Items(BaseModel):
    code: str = 'CD001' #code
    account_num: str = 'ABCD1234'
    base_date: int = 970328
    increase_closing_amt: float = 20000.00
    decrease_closing_amt: float = 20000.00
    withdraw_reason: str = 'N1'
    settlement_info_cnt: int = 2
    settlement_info: Union[List[SettlementInfo], None] = [
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
    settlement_info_rffp: Union[List[SettlementInfoRffp], None] = [
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
    deposit_requirement_change_details: Union[List[DepositRequirementChangeDetails], None] = [
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
    

@app.post('/deposit/invr_dpsa/transfer/closing_and_reserve_for_payment')
async def postIndex(reqItems: Req012Items):
    print('REQ >>>', reqItems)
    dic = json.loads(getResJson('012'))
    dic['rsp_code'] = reqItems.code
    return dic


# --- 013 : POST
class Req013Items(BaseModel):
    code: str = 'CD001' #code
    account_num: str = 'ABCD1234'
    tran_idn_num: str = 'ABC111'


@app.post('/deposit/invr_dpsa/transfer/closing_cancel')
async def postIndex(reqItems: Req013Items):
    print('REQ >>>', reqItems)
    dic = json.loads(getResJson('013'))
    dic['rsp_code'] = reqItems.code
    return dic


# --- 014 : GET
@app.get('/deposit/invr_dpsa/transfer/closing_transaction_list')
async def getIndex(tran_date: int, dps_mth_dscd: str, prod_code: str, search_type: str, before_inquiry_trace_info: str):
    print('REQ >>>', tran_date, dps_mth_dscd, prod_code, search_type, before_inquiry_trace_info)
    return json.loads(getResJson('014'))


# --- 015 : GET
@app.get('/deposit/invr_dpsa/account/transaction_list')
async def getIndex(account_num: str, currency_code: str, from_date: int, to_date:int, before_inquiry_trace_info: str):
    print('REQ >>>', account_num, currency_code, from_date, to_date, before_inquiry_trace_info)
    return json.loads(getResJson('015'))


# --- 016 : GET
@app.get('/deposit/invr_dpsa/account/interest_dividend_list')
async def getIndex(account_num: str, currency_code: str, search_year: int):
    print('REQ >>>', account_num, currency_code, search_year)
    return json.loads(getResJson('016'))


# --- 017 : GET
@app.get('/deposit/invr_dpsa/account/estimated_interest')
async def getIndex(account_num: str):
    print('REQ >>>', account_num)
    return json.loads(getResJson('017'))


# --- 018 : GET
@app.get('/deposit/invr_dpsa/account/balance_daily')
async def getIndex(account_num: str, currency_code: str, from_date: int, to_date: int, before_inquiry_trace_info: str):
    print('REQ >>>', account_num, currency_code, from_date, to_date, before_inquiry_trace_info)
    return json.loads(getResJson('018'))


# --- 019 : GET
@app.get('/deposit/invr_dpsa/account/average_balance_yearly')
async def getIndex(account_num: str, currency_code: int, search_year: int):
    print('REQ >>>', account_num, currency_code, search_year)
    return json.loads(getResJson('019'))


# --- 020 : GET
@app.get('/deposit/invr_dpsa/account/average_balance_quarterly')
async def getIndex(account_num: str, currency_code: str, search_year: int):
    print('REQ >>>', account_num, currency_code, search_year)
    return json.loads(getResJson('020'))


# --- 021 : GET
@app.get('/deposit/invr_dpsa/account/average_balance_monthly')
async def getIndex(account_num: str, currency_code: str, search_year: int):
    print('REQ >>>', account_num, currency_code, search_year)
    return json.loads(getResJson('021'))
