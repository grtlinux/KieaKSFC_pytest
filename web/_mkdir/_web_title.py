#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
# end of header
"""
program: _web_title.py
    ENV:
        VSC Editor Encoding: UTF-8
        installed : beautifulsoup4, requests, requests-file
    RUN:
        $ pip install beautifulsoup4 requests requests-file
        $ python -V
            Python 3.10.9
        $ python _web_title.py
"""
import os
import requests
from requests_file import FileAdapter
from bs4 import BeautifulSoup as bs

# ----------------------------------------------------------
PWD = os.getcwd()

# ----------------------------------------------------------
def get_url_contents(url):
    '''
        status_code, text = get_url_contents('file:///etc/hosts')
        status_code, text = get_url_contents('http://localhost:8080/_web_css.html')
    '''
    reqSession = None
    try:
        reqSession = requests.Session()
        if url.lower().startswith('file://'):
            reqSession.mount('file://', FileAdapter())
        response = reqSession.get(url)
        # return response.status_code, response.text
        return response
    finally:
        if reqSession is not None:
            reqSession.close()

# ----------------------------------------------------------
def test00():
    pwd = os.getcwd()
    print('>>> pwd:', pwd)
    pass
'''
'''
# ----------------------------------------------------------
def test01():
    reqSession = requests.Session()
    reqSession.mount('file://', FileAdapter())
    response = reqSession.get('file://' + PWD + '/_web_css.html')
    # response = session.get('file://./_web_css.html')  # ERROR
    print(response)
    if response.status_code / 100 == 2:
        print('>>>>>', response.text)
    pass
'''
'''
# ----------------------------------------------------------
def test02():
    reqSession = requests.Session()
    response = reqSession.get('http://localhost:8080/_web_css.html')
    # response = session.get('file://./_web_css.html')  # ERROR
    print(response)
    if response.status_code / 100 == 2:
        print('>>>>>', response.text)
    pass
'''
'''
# ----------------------------------------------------------
def test03():
    response = get_url_contents('file://' + PWD + '/_web_title.html')
    if response.status_code / 100 == 2:
        # print('>>>>>', response.text)
        soup = bs(response.text, 'html.parser')
        # print(soup.prettify())
        # return
        # elements = soup.select('h2',)
        # elements = soup.select('a',)
        elements = soup.select('a',{'target':'_top'})
        for index, element in enumerate(elements, 1):
            title = element.text.replace(' ', '_').strip()
            href = element.get('href')
            # href = element.attris['href']
            print('{}: {}\t{}'.format(index, title, href))
    pass
'''
'''
# ----------------------------------------------------------
def test04():
    response = get_url_contents('file://' + PWD + '/_web_title.html')
    if response.status_code / 100 == 2:
        soup = bs(response.text, 'html.parser')
        elements = soup.findAll('a',{'target':'_top'})
        # elements = soup.find_all('*')
        for index, element in enumerate(elements, 1):
            title = element.text.replace(' ', '_').strip()
            # href = element.get('href')
            href = element.attrs['href']
            print('{}: {}\t{}'.format(index, title, href))
    pass
'''
'''
# ----------------------------------------------------------
_H2_TEXT = None
_LINK_LST = []
# ----------------------------------------------------------
def test05_h2(line):
    global _H2_TEXT
    soup = bs(line, 'html.parser')
    elements = soup.findAll('h2',{})
    _H2_TEXT = elements[0].text
    _LINK_LST.clear()
    # print(_H2_TEXT)
    pass
'''
'''
# ----------------------------------------------------------
def test05_a(line):
    global _LINK_LST
    if _H2_TEXT is None: return
    _LINK_LST.append(line)
    pass
'''
'''
# ----------------------------------------------------------
def test05_br(line):
    global _LINK_LST
    soup = bs('\n'.join(_LINK_LST), 'html.parser')
    elements = soup.findAll('a',{})
    print('\n>>>>> title:', _H2_TEXT)
    for index, element in enumerate(elements, 1):
        title = '%03d_'%index + element.text.replace(' ', '_').strip() + '_01'
        print('\t{}: {}'.format(index, title))
        # href = element.get('href')
        # print('{}: {}\t{}'.format(index, title, href))
    pass
'''
'''
# ----------------------------------------------------------
def test05():
    fileName = PWD + '/_web_title.html'
    with open(fileName, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line == '': continue
            # print(line)

            if line.startswith('<h2>'):
                test05_h2(line)
            elif line.startswith('<a '):
                test05_a(line)
            elif line.startswith('<br>'):
                test05_br(line)
    pass
'''
'''
# ----------------------------------------------------------
if __name__ == '__main__':
    # test00()
    # test01()
    # test02()
    # test03()
    # test04()
    test05()
'''
'''



