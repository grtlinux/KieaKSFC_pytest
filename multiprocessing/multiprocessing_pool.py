#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: multiprocessing_pool.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python multiprocessing_pool.py
"""
import multiprocessing

def do_calculation(data):
    return data * 2

def start_process():
    print('Starting', multiprocessing.current_process().name)

if __name__ == '__main__':
    inputs = list(range(10))
    print('Input   :', inputs)

    builtin_outputs = map(do_calculation, inputs)
    print('Built-in:', builtin_outputs)

    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_size, initializer=start_process,)
    pool_outputs = pool.map(do_calculation, inputs)
    pool.close()  # no more tasks
    pool.join()  # wrap up current tasks

    print('Pool    :', pool_outputs)
'''
SpawnPoolWorker-2 processing 0
SpawnPoolWorker-2 processing 1
SpawnPoolWorker-2 processing 2
SpawnPoolWorker-2 processing 3
SpawnPoolWorker-2 processing 4
SpawnPoolWorker-2 processing 5
SpawnPoolWorker-2 processing 6
SpawnPoolWorker-2 processing 7
SpawnPoolWorker-2 processing 8
SpawnPoolWorker-2 processing 9
SpawnPoolWorker-2 processing 10
SpawnPoolWorker-2 processing 11
SpawnPoolWorker-2 processing 12
SpawnPoolWorker-2 processing 13
SpawnPoolWorker-2 processing 14
SpawnPoolWorker-3 processing 21
SpawnPoolWorker-3 processing 22
SpawnPoolWorker-3 processing 23
SpawnPoolWorker-3 processing 24
SpawnPoolWorker-3 processing 25
SpawnPoolWorker-3 processing 26
SpawnPoolWorker-3 processing 27
SpawnPoolWorker-3 processing 28
SpawnPoolWorker-3 processing 29
SpawnPoolWorker-3 processing 30
SpawnPoolWorker-3 processing 31
SpawnPoolWorker-3 processing 32
SpawnPoolWorker-3 processing 33
SpawnPoolWorker-3 processing 34
SpawnPoolWorker-3 processing 35
SpawnPoolWorker-3 processing 36
SpawnPoolWorker-3 processing 37
SpawnPoolWorker-3 processing 38
SpawnPoolWorker-3 processing 39
SpawnPoolWorker-3 processing 40
SpawnPoolWorker-3 processing 41
SpawnPoolWorker-3 processing 42
SpawnPoolWorker-3 processing 43
SpawnPoolWorker-3 processing 44
SpawnPoolWorker-3 processing 45
SpawnPoolWorker-3 processing 46
SpawnPoolWorker-3 processing 47
SpawnPoolWorker-3 processing 48
SpawnPoolWorker-3 processing 49
SpawnPoolWorker-3 processing 50
SpawnPoolWorker-3 processing 51
SpawnPoolWorker-3 processing 52
SpawnPoolWorker-3 processing 53
SpawnPoolWorker-3 processing 54
SpawnPoolWorker-3 processing 55
SpawnPoolWorker-1 processing 56
SpawnPoolWorker-2 processing 15
SpawnPoolWorker-1 processing 57
SpawnPoolWorker-1 processing 58
SpawnPoolWorker-3 processing 63
SpawnPoolWorker-1 processing 59
SpawnPoolWorker-1 processing 60
SpawnPoolWorker-1 processing 61
SpawnPoolWorker-3 processing 64
SpawnPoolWorker-1 processing 62
SpawnPoolWorker-3 processing 65
SpawnPoolWorker-3 processing 66
SpawnPoolWorker-3 processing 67
SpawnPoolWorker-3 processing 68
SpawnPoolWorker-3 processing 69
SpawnPoolWorker-1 processing 70
SpawnPoolWorker-1 processing 71
SpawnPoolWorker-1 processing 72
SpawnPoolWorker-1 processing 73
SpawnPoolWorker-1 processing 74
SpawnPoolWorker-1 processing 75
SpawnPoolWorker-1 processing 76
SpawnPoolWorker-2 processing 16
SpawnPoolWorker-3 processing 77
SpawnPoolWorker-3 processing 78
SpawnPoolWorker-3 processing 79
SpawnPoolWorker-3 processing 80
SpawnPoolWorker-3 processing 81
SpawnPoolWorker-3 processing 82
SpawnPoolWorker-3 processing 83
SpawnPoolWorker-1 processing 84
SpawnPoolWorker-1 processing 85
SpawnPoolWorker-1 processing 86
SpawnPoolWorker-1 processing 87
SpawnPoolWorker-1 processing 88
SpawnPoolWorker-1 processing 89
SpawnPoolWorker-1 processing 90
SpawnPoolWorker-3 processing 91
SpawnPoolWorker-3 processing 92
SpawnPoolWorker-3 processing 93
SpawnPoolWorker-3 processing 94
SpawnPoolWorker-3 processing 95
SpawnPoolWorker-3 processing 96
SpawnPoolWorker-3 processing 97
SpawnPoolWorker-2 processing 17
SpawnPoolWorker-2 processing 18
SpawnPoolWorker-2 processing 19
SpawnPoolWorker-2 processing 20
SpawnPoolWorker-3 processing 98
SpawnPoolWorker-3 processing 99
Pool    : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]
'''