#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
program: find_files01.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ python -V
            Python 3.10.9

        $ tree imsi
            imsi
            ├── a01.java
            ├── b.01.java
            └── sub
                ├── a02.java
                └── c02.java

        $ python find_files01.py
            FILE: /Users/kang-air/KANG/_GIT_HUB/python/github/KieaKSFC_pyfep/find_files/find_files01.py
            FILE: find_files01.py
            >>> /Users/kang-air/KANG/_GIT_HUB/python/github/imsi ['sub'] ['a01.java', 'b.01.java']
            >>> /Users/kang-air/KANG/_GIT_HUB/python/github/imsi/sub [] ['c02.java', 'a02.java']

            /Users/kang-air/KANG/_GIT_HUB/python/github/imsi/a01.java
            /Users/kang-air/KANG/_GIT_HUB/python/github/imsi/b.01.java
            /Users/kang-air/KANG/_GIT_HUB/python/github/imsi/sub/c02.java
            /Users/kang-air/KANG/_GIT_HUB/python/github/imsi/sub/a02.java
"""
import os

# ------------------------------------------
def find_java_files(path):
    ''' find_java_files '''
    java_files = []
    for root, dirs, files in os.walk(path):
        print('>>>', root, dirs, files)
        for file in files:
            if file.endswith(".java"):
                java_files.append(os.path.join(root, file))
    return java_files

# ------------------------------------------
def main():
    ''' main '''
    print('FILE:', __file__)
    print('FILE:', __file__.split(os.sep)[-1])
    # print('FILE:', __file__.split(os.sep).reverse())
    # print('FILE:', __file__.split('/')[-1])
    # print('FILE:', __file__.split('/').reverse()[1]) # error
    # print('FILE:', __file__[__file__.rfind('/')+1:])
    target_directory = "/Users/kang-air/KANG/_GIT_HUB/python/github/imsi"
    java_files = find_java_files(target_directory)
    print()

    for java_file in java_files:
        print(java_file)

# ------------------------------------------
if __name__ == "__main__":
    main()
