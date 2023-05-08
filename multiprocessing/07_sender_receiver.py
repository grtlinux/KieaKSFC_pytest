#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 07_sender_receiver.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 07_sender_receiver.py
"""
from time import sleep
from random import random
from multiprocessing import Process, Pipe

# generate work
def sender(connection):
    print('Sender: Running', flush=True)
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block
        sleep(value)
        # send a value
        connection.send(value)
    # all done
    connection.send(None)
    print('Sender: Done', flush=True)

# comsumer work
def receiver(connection):
    print('Receiver: Running', flush=True)
    # consumer work
    while True:
        # get a unit of work
        item = connection.recv()
        # report
        print(f'>receiver got {item}', flush=True)
        # check for stop
        if item is None:
            break
    # all done
    print('Receiver: Done', flush=True)

# main: entry point
if __name__ == '__main__':
    conn1, conn2 = Pipe()

    sender_process = Process(target=sender, args=(conn2,))
    sender_process.start()

    receiver_process = Process(target=receiver, args=(conn1,))
    receiver_process.start()

    sender_process.join()
    receiver_process.join()
'''
Sender: Running
Receiver: Running
>receiver got 0.7999181129036536
>receiver got 0.4843081463472746
>receiver got 0.7482572505467575
>receiver got 0.5309697251362377
>receiver got 0.0010111195865465383
>receiver got 0.551648917100208
>receiver got 0.3043048560110908
>receiver got 0.6786767880731632
>receiver got 0.949040728917034
Sender: Done
>receiver got 0.2606097252015622
>receiver got None
Receiver: Done
'''