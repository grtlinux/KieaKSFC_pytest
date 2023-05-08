#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016-2020,2021,2022,2023 TAIN Inc. All rights reserved.
#
#end_pymotw_header
# file: .pylintrc
"""
comment: Spawn a Process – Chapter 3: Process Based Parallelism
program: fetch_podcasts.py
    ENV:
        VSC Editor Encoding: UTF-8
    RUN:
        $ pip install feedparser
        $ python -V
            Python 3.10.9
        $ python fetch_podcasts.py
        < create mp3 files >
"""
from queue import Queue
import threading
import time
import urllib
from urllib.parse import urlparse

import feedparser

# Set up some global variables
num_fetch_threads = 2
enclosure_queue = Queue()

# A real app wouldn't use hard-coded data...
feed_urls = [
    'http://talkpython.fm/episodes/rss',
]


def message(s):
    print('{}: {}'.format(threading.current_thread().name, s))


def download_enclosures(queue):
    """This is the worker thread function.
    It processes items in the queue one after
    another.  These daemon threads go into an
    infinite loop, and exit only when
    the main thread ends.
    """
    while True:
        message('looking for the next enclosure')
        url = queue.get()
        filename = url.rpartition('/')[-1]
        message('downloading {}'.format(filename))
        response = urllib.request.urlopen(url)
        data = response.read()
        # Save the downloaded file to the current directory
        message('writing to {}'.format(filename))
        with open(filename, 'wb') as outfile:
            outfile.write(data)
        queue.task_done()


# Set up some threads to fetch the enclosures
for i in range(num_fetch_threads):
    worker = threading.Thread(
        target=download_enclosures,
        args=(enclosure_queue,),
        name='worker-{}'.format(i),
    )
    worker.daemon = True
    worker.start()

# Download the feed(s) and put the enclosure URLs into
# the queue.
for url in feed_urls:
    response = feedparser.parse(url, agent='fetch_podcasts.py')
    for entry in response['entries'][:5]:
        for enclosure in entry.get('enclosures', []):
            parsed_url = urlparse(enclosure['url'])
            message('queuing {}'.format(parsed_url.path.rpartition('/')[-1]))
            enclosure_queue.put(enclosure['url'])

# Now wait for the queue to be empty, indicating that we have
# processed all of the downloads.
message('*** main thread waiting')
enclosure_queue.join()
message('*** done')
'''
worker-0: looking for the next enclosure
worker-1: looking for the next enclosure
MainThread: queuing a-stroll-down-startup-lane.mp3
MainThread: queuing live-from-pycon-2023.mp3
MainThread: queuing pep-711-distributing-python-binaries.mp3
MainThread: queuing things-i-wish-someone-had-explained-to-me-sooner-about-python.mp3
worker-1: downloading a-stroll-down-startup-lane.mp3
worker-0: downloading live-from-pycon-2023.mp3
MainThread: queuing the-intersection-of-tabular-data-and-generative-ai.mp3
MainThread: *** main thread waiting
worker-0: writing to live-from-pycon-2023.mp3
worker-0: looking for the next enclosure
worker-0: downloading pep-711-distributing-python-binaries.mp3
worker-0: writing to pep-711-distributing-python-binaries.mp3
worker-0: looking for the next enclosure
worker-0: downloading things-i-wish-someone-had-explained-to-me-sooner-about-python.mp3
worker-0: writing to things-i-wish-someone-had-explained-to-me-sooner-about-python.mp3
worker-0: looking for the next enclosure
worker-0: downloading the-intersection-of-tabular-data-and-generative-ai.mp3
worker-0: writing to the-intersection-of-tabular-data-and-generative-ai.mp3
worker-0: looking for the next enclosure
worker-1: writing to a-stroll-down-startup-lane.mp3
worker-1: looking for the next enclosure
MainThread: *** done
'''