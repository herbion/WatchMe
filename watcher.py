# -*- coding: utf-8 -*-
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from datetime import datetime

"""
Created on Sat Mar 31 00:37:08 2012

@author: herbion
"""

__author__ = 'herbion'


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print event
    def on_deleted(self, event):
        print event
    def on_moved(self, event):
        print event
    def on_modified(self, event):
        print event
    def log(self, e):
        print getCurrentTime(), e
def getCurrentTime():
    time = datetime.now()
    return "[%d:%d:%d]" % (time.hour, time.minute, time.second)

watch = 'C:\\watch'
observer = Observer()
observer.schedule(Handler(), path = watch , recursive=True)
observer.start()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    observer.stop()
observer.join()