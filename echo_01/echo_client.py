#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: echo_client.py
'''
program: echo_client.py
comment:
    $ python3 echo_client.py
'''
import socket

HOST = '127.0.0.1'
PORT = 6000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'0015Hello, world!!!')
    data = s.recv(1024)

print('received', repr(data))
