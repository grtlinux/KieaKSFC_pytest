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
    lstBytes = [b'abc', b'def', b'ghi']
    print('1>', type(lstBytes), lstBytes)
    bData = b''.join(lstBytes)
    print('1>', type(bData), bData)
    print('-' * 60)
    pass
'''
1> <class 'list'> [b'abc', b'def', b'ghi']
1> <class 'bytes'> b'abcdefghi'
'''

# ------------------------------------------------------------
def test02() -> None:
    ''' test02 function '''
    lstBytes = [b'abc', 'def', b'ghi']
    print('1>', type(lstBytes), lstBytes)
    bData = b''.join(lstBytes)  # TypeError: sequence item 0: expected bytes instance, str found
    bData = ''.join(lstBytes)   # TypeError: sequence item 0: expected str instance, bytes found
    print('1>', type(bData), bData)
    print('-' * 60)
    pass
'''
1> <class 'list'> [b'abc', 'def', b'ghi']
Traceback (most recent call last):
  File "/Users/kang-air/KANG/_GIT_HUB/python/github/KieaKSFC_pytest/bArr_join/bArr_join.py", line 49, in <module>
    main()
  File "/Users/kang-air/KANG/_GIT_HUB/python/github/KieaKSFC_pytest/bArr_join/bArr_join.py", line 44, in main
    if True: test02()
  File "/Users/kang-air/KANG/_GIT_HUB/python/github/KieaKSFC_pytest/bArr_join/bArr_join.py", line 35, in test02
    bData = ''.join(lstBytes)
TypeError: sequence item 0: expected str instance, bytes found
'''
# ------------------------------------------------------------
def main() -> None:
    '''main function'''
    if True: test01()
    if True: test02()
    pass

# ------------------------------------------------------------
if __name__ == '__main__':
    main()
'''
'''