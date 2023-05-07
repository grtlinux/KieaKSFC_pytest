#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: evaluating_performances.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python evaluating_performances.py
"""
from threading import Thread
import multiprocessing

def show_results(func_name, results):
    print("%-23s %4.6f seconds" % (func_name, results))
    # print(f'{func_name}:\n'
    #       f'\tcount: {len(results)}\n'
    #       f'\tresults: {results}\n'
    #       f'\tsum: {sum(results)}')

class process_object(multiprocessing.Process):
    def __init__(self, func):
        multiprocessing.Process.__init__(self)
        self.func = func
    
    def run(self):
        self.func()

def process(num_processes, func):
    funcs = []
    for i in range(int(num_processes)):
        funcs.append(process_object(func))
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()

class thread_object(Thread):
    def __init__(self,
                 group=None,
                 target=None,
                 name=None,
                 args=(),
                 kwargs=None,
                 *,
                 daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs
    
    def run(self):
        self.args[0]()

def threaded(num_threads, func):
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(thread_object(args=(func,)))
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()

class non_object(object):
    def __init__(self, func):
        self.func = func
    
    def run(self):
        self.func()

def non(num_non, func):
    funcs = []
    for i in range(int(num_non)):
        funcs.append(non_object(func))
    for i in funcs:
        i.run()

def function_to_run():
    pass

def function_to_run2():
    a, b = 1, 1
    for _ in range(10000):
        a, b = b, a + b

def function_to_run3():
    from urllib import request
    response = request.urlopen('http://www.baidu.com/')
    response.read(1024)

if __name__ == '__main__':
    import sys
    from timeit import Timer

    repeat = 10
    number = 1
    num = [1, 2, 4, 8]

    for func in [function_to_run, function_to_run2, function_to_run3]:
        for i in num:
            t = Timer("non(%s, %s)" % (i, func.__name__),
                        "from __main__ import non",
                        globals=globals())
            best_result = min(t.repeat(repeat=repeat, number=number))
            show_results("non (%s iters)" % i, best_result)
            
            t = Timer("threaded(%s, %s)" % (i, func.__name__),
                      "from __main__ import threaded",
                      globals=globals())
            best_result = min(t.repeat(repeat=repeat, number=number))
            show_results("threaded (%s threads)" % i, best_result)

            t = Timer("process(%s, %s)" % (i, func.__name__),
                      "from __main__ import process",
                      globals=globals())
            best_result = min(t.repeat(repeat=repeat, number=number))
            show_results("process (%s process)" % i, best_result)
        print('Iterations complete')
'''
non (1 iters)           0.000001 seconds
threaded (1 threads)    0.000122 seconds
process (1 process)     0.052213 seconds
non (2 iters)           0.000002 seconds
threaded (2 threads)    0.000150 seconds
process (2 process)     0.067258 seconds
non (4 iters)           0.000006 seconds
threaded (4 threads)    0.000366 seconds
process (4 process)     0.120709 seconds
non (8 iters)           0.000012 seconds
threaded (8 threads)    0.000748 seconds
process (8 process)     0.255639 seconds
Iterations complete
non (1 iters)           0.003304 seconds
threaded (1 threads)    0.003268 seconds
process (1 process)     0.062753 seconds
non (2 iters)           0.005123 seconds
threaded (2 threads)    0.005429 seconds
process (2 process)     0.077083 seconds
non (4 iters)           0.011228 seconds
threaded (4 threads)    0.010526 seconds
process (4 process)     0.136281 seconds
non (8 iters)           0.020851 seconds
threaded (8 threads)    0.023607 seconds
process (8 process)     0.290138 seconds
Iterations complete
non (1 iters)           0.150530 seconds
threaded (1 threads)    0.160840 seconds
process (1 process)     0.285358 seconds
non (2 iters)           0.327576 seconds
threaded (2 threads)    0.171617 seconds
process (2 process)     0.308870 seconds
non (4 iters)           0.686249 seconds
threaded (4 threads)    0.168842 seconds
process (4 process)     0.388263 seconds
non (8 iters)           1.426957 seconds
threaded (8 threads)    0.185979 seconds
process (8 process)     0.582316 seconds
Iterations complete
'''


