#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: test_gen_yield.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python test_gen_yield.py
"""
def gen():
    yield 1
    yield 2
    yield 3

print(gen())
print(type(gen()))
print(list(gen()))
print()

for i in gen():
    print(i)
print()

g = gen()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
print()

def gen_even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for i in gen_even(10):
    print(i)
'''
<generator object gen at 0x103e36570>
<class 'generator'>
[1, 2, 3]

1
2
3

1
2
3

0
2
4
6
8
'''