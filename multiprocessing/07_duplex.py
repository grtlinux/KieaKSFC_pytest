#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 07_duplex.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 07_duplex.py
"""
# example of using a duplex pipe between processes
from time import sleep
from random import random
from multiprocessing import Process, Pipe
 
# generate and send a value
def generate_send(connection, value):
    # generate value
    new_value = random()
    # block
    sleep(new_value)
    # update value
    value = value + new_value
    # report
    print(f'>sending {value}', flush=True)
    # send value
    connection.send(value)
 
# ping pong between processes
def pingpong(connection, send_first):
    print('Process Running', flush=True)
    # check if this process should seed the process
    if send_first:
        generate_send(connection, 0)
    # run until limit reached
    while True:
        # read a value
        value = connection.recv()
        # report
        print(f'>received {value}', flush=True)
        # send the value back
        generate_send(connection, value)
        # check for stop
        if value > 10:
            break
    print('Process Done', flush=True)
 
# entry point
if __name__ == '__main__':
    # create the pipe
    conn1, conn2 = Pipe(duplex=True)
    # create players
    player1 = Process(target=pingpong, args=(conn1,True))
    player2 = Process(target=pingpong, args=(conn2,False))
    # start players
    player1.start()
    player2.start()
    # wait for players to finish
    player1.join()
    player2.join()
'''
Process Running
Process Running
>sending 0.2700265408815137
>received 0.2700265408815137
>sending 0.9410083889473474
>received 0.9410083889473474
>sending 1.895144835734302
>received 1.895144835734302
>sending 2.345686987497196
>received 2.345686987497196
>sending 3.2255224833680627
>received 3.2255224833680627
>sending 3.4916095816037727
>received 3.4916095816037727
>sending 4.097470896533035
>received 4.097470896533035
>sending 4.378141555442375
>received 4.378141555442375
>sending 5.301979259193961
>received 5.301979259193961
>sending 5.634148250357562
>received 5.634148250357562
>sending 5.922764496745184
>received 5.922764496745184
>sending 5.927771069136024
>received 5.927771069136024
>sending 6.420428824056882
>received 6.420428824056882
>sending 6.626603391733651
>received 6.626603391733651
>sending 7.306191419272462
>received 7.306191419272462
>sending 8.085651013807892
>received 8.085651013807892
>sending 9.052106041923743
>received 9.052106041923743
>sending 9.149830030458542
>received 9.149830030458542
>sending 9.42667279536582
>received 9.42667279536582
>sending 9.583566934720814
>received 9.583566934720814
>sending 10.477314302836117
>received 10.477314302836117
>sending 11.132028036058854
Process Done
>received 11.132028036058854
>sending 11.801506692809959
Process Done
'''