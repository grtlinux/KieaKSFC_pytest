#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: 06_using_queue.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 06_using_queue.py
"""
import multiprocessing
import random
import time

class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
    
    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print(f'Process Producer: item {item} appended to queue {self.name}')
            time.sleep(1)
            # print(f'The size of queue is {self.queue.qsize()}')

class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
    
    def run(self):
        time.sleep(5)
        while True:
            if self.queue.empty():
                print(f'The queue is empty')
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print(f'Process Consumer: item {item} popped from by {self.name} queue {self.name}')
                time.sleep(1)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
'''
Process Producer: item 45 appended to queue Producer-1
Process Producer: item 225 appended to queue Producer-1
Process Producer: item 114 appended to queue Producer-1
Process Producer: item 255 appended to queue Producer-1
Process Producer: item 122 appended to queue Producer-1
Process Producer: item 209 appended to queue Producer-1
Process Producer: item 29 appended to queue Producer-1
Process Consumer: item 45 popped from by Consumer-2 queue Consumer-2
Process Producer: item 235 appended to queue Producer-1
Process Producer: item 124 appended to queue Producer-1
Process Producer: item 20 appended to queue Producer-1
Process Consumer: item 225 popped from by Consumer-2 queue Consumer-2
Process Consumer: item 114 popped from by Consumer-2 queue Consumer-2
Process Consumer: item 255 popped from by Consumer-2 queue Consumer-2
Process Consumer: item 122 popped from by Consumer-2 queue Consumer-2
Process Consumer: item 209 popped from by Consumer-2 queue Consumer-2
Process Consumer: item 29 popped from by Consumer-2 queue Consumer-2
Process Consumer: item 235 popped from by Consumer-2 queue Consumer-2
Process Consumer: item 124 popped from by Consumer-2 queue Consumer-2
Process Consumer: item 20 popped from by Consumer-2 queue Consumer-2
The queue is empty
'''