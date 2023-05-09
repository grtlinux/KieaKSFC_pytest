#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: 10_process_pool.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9
        $ python 10_process_pool.py
"""
import multiprocessing

def function_square(data):
    name = multiprocessing.current_process().name
    print ('%s processing %s' % (name, data))
    result = data * data
    return result

if __name__ == '__main__':
    inputs = list(range(0, 100))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)

    pool.close()
    pool.join()
    print ('Pool    :', pool_outputs)
'''
SpawnPoolWorker-1 processing 0
SpawnPoolWorker-1 processing 1
SpawnPoolWorker-1 processing 2
SpawnPoolWorker-1 processing 3
SpawnPoolWorker-1 processing 4
SpawnPoolWorker-1 processing 5
SpawnPoolWorker-1 processing 6
SpawnPoolWorker-1 processing 7
SpawnPoolWorker-1 processing 8
SpawnPoolWorker-1 processing 9
SpawnPoolWorker-1 processing 10
SpawnPoolWorker-1 processing 11
SpawnPoolWorker-1 processing 12
SpawnPoolWorker-1 processing 13
SpawnPoolWorker-1 processing 14
SpawnPoolWorker-1 processing 15
SpawnPoolWorker-1 processing 16
SpawnPoolWorker-1 processing 17
SpawnPoolWorker-1 processing 18
SpawnPoolWorker-1 processing 19
SpawnPoolWorker-1 processing 20
SpawnPoolWorker-1 processing 21
SpawnPoolWorker-1 processing 22
SpawnPoolWorker-1 processing 23
SpawnPoolWorker-1 processing 24
SpawnPoolWorker-1 processing 25
SpawnPoolWorker-1 processing 26
SpawnPoolWorker-1 processing 27
SpawnPoolWorker-1 processing 28
SpawnPoolWorker-1 processing 29
SpawnPoolWorker-1 processing 30
SpawnPoolWorker-1 processing 31
SpawnPoolWorker-1 processing 32
SpawnPoolWorker-1 processing 33
SpawnPoolWorker-1 processing 34
SpawnPoolWorker-1 processing 35
SpawnPoolWorker-1 processing 36
SpawnPoolWorker-1 processing 37
SpawnPoolWorker-1 processing 38
SpawnPoolWorker-1 processing 39
SpawnPoolWorker-1 processing 40
SpawnPoolWorker-1 processing 41
SpawnPoolWorker-1 processing 42
SpawnPoolWorker-1 processing 43
SpawnPoolWorker-1 processing 44
SpawnPoolWorker-1 processing 45
SpawnPoolWorker-1 processing 46
SpawnPoolWorker-1 processing 47
SpawnPoolWorker-1 processing 48
SpawnPoolWorker-1 processing 49
SpawnPoolWorker-1 processing 50
SpawnPoolWorker-1 processing 51
SpawnPoolWorker-1 processing 52
SpawnPoolWorker-1 processing 53
SpawnPoolWorker-1 processing 54
SpawnPoolWorker-1 processing 55
SpawnPoolWorker-1 processing 56
SpawnPoolWorker-1 processing 57
SpawnPoolWorker-1 processing 58
SpawnPoolWorker-1 processing 59
SpawnPoolWorker-1 processing 60
SpawnPoolWorker-1 processing 61
SpawnPoolWorker-1 processing 62
SpawnPoolWorker-1 processing 63
SpawnPoolWorker-1 processing 64
SpawnPoolWorker-1 processing 65
SpawnPoolWorker-1 processing 66
SpawnPoolWorker-1 processing 67
SpawnPoolWorker-1 processing 68
SpawnPoolWorker-1 processing 69
SpawnPoolWorker-1 processing 70
SpawnPoolWorker-1 processing 71
SpawnPoolWorker-1 processing 72
SpawnPoolWorker-1 processing 73
SpawnPoolWorker-1 processing 74
SpawnPoolWorker-1 processing 75
SpawnPoolWorker-1 processing 76
SpawnPoolWorker-1 processing 77
SpawnPoolWorker-1 processing 78
SpawnPoolWorker-1 processing 79
SpawnPoolWorker-1 processing 80
SpawnPoolWorker-1 processing 81
SpawnPoolWorker-1 processing 82
SpawnPoolWorker-1 processing 83
SpawnPoolWorker-1 processing 84
SpawnPoolWorker-1 processing 85
SpawnPoolWorker-1 processing 86
SpawnPoolWorker-1 processing 87
SpawnPoolWorker-1 processing 88
SpawnPoolWorker-1 processing 89
SpawnPoolWorker-1 processing 90
SpawnPoolWorker-1 processing 91
SpawnPoolWorker-1 processing 92
SpawnPoolWorker-1 processing 93
SpawnPoolWorker-1 processing 94
SpawnPoolWorker-1 processing 95
SpawnPoolWorker-1 processing 96
SpawnPoolWorker-1 processing 97
SpawnPoolWorker-1 processing 98
SpawnPoolWorker-1 processing 99
Pool    : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]
'''