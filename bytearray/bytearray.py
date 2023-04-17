#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: bArr_join.py
'''
program: bArr_join.py
comment:
    $ python -V
        Python 3.10.9
    $ python bArr_join.py
'''

# ------------------------------------------------------------
def test01() -> None:
    ''' test01 function '''
    print('1>', bytes(10))   # 0이 10개 들어있는 바이트 객체 생성
    print('1>', bytes([10, 20, 30, 40, 50]))   # 리스트로 바이트 객체 생성
    print('1>', bytes(b'hello'))    # 바이트 객체로 바이트 객체 생성

    print('1>', '-' * 40)
    pass
'''
'''

# ------------------------------------------------------------
def test02() -> None:
    ''' test02 function bytearray 각 항목을 변경할 수 있다. '''
    print('2>', bytearray())
    print('2>', bytearray(5))
    print('2>', bytearray([10,20,30,40,50]))
    print('2>', bytearray(b'test. hello'))

    x = bytearray(b'hello')
    x[0] = ord('H')
    print('2>', type(x), x)

    print('2>', '-' * 40)
    pass
'''
'''

# ------------------------------------------------------------
def test03() -> None:
    ''' test03 function encode(str -> bytes), decode(bytes -> str) '''
    print('3>', 'hello'.encode())     # str을 bytes로 변환
    print('3>', b'hello'.decode())    # bytes를 str로 변환

    print('3>', '안녕'.encode('euc-kr'))
    print('3>', '안녕'.encode('utf-8'))

    x = '안녕'.encode('euc-kr')
    print('3>', x.decode('euc-kr'))
    y = '안녕'.encode('utf-8')
    print('3>', y.decode('utf-8'))

    print('3>', bytes('안녕', encoding='euc-kr'))
    print('3>', bytearray('안녕', encoding='cp949'))    # cp949는 euc-kr과 동일. CP949는 마이크로소프트에서 만든 한글 인코딩의 한 종류이며 EUC-KR의 확장형입니다(Windows에서 사용)

    print('3>', '-' * 40)
    pass
'''
'''

# ------------------------------------------------------------
def test04() -> None:
    ''' test04 function '''
    bText = "한글".encode('utf-8')
    print('4>', bText)
    print('4>', bText.decode())
    # print('4>', bText.decode('euc-kr'))  # UnicodeDecodeError: 'euc_kr' codec can't decode byte 0x8b in position 0: illegal multibyte sequence
    print('4>', bText.decode('utf-8'))

    print('4>', '-' * 40)
    pass
'''
'''

# ------------------------------------------------------------
def test05() -> None:
    ''' test05 function '''
    lstBytes = [b'000REQ1234567890', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ', b'abcdefghijklmnopqrstuvwxyz', b'0123456789', b'!@#$%^&*()_+']
    bsStream = bytearray(b''.join(lstBytes))
    bsStream[:3] = b'123'
    stream = bsStream.decode()
    print('5>', type(stream), stream)

    print('5>', '-' * 40)
    pass
'''
'''

# ------------------------------------------------------------
def main() -> None:
    '''main function'''
    if True: test01()
    if True: test02()
    if True: test03()
    if True: test04()
    if True: test05()
    pass

# ------------------------------------------------------------
if __name__ == '__main__':
    main()
'''
'''