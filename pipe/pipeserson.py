#!/usr/bin/python
#coding:utf-8

import os

pipe_file = '/root/current/10-26/pipefile'

fd_r = os.open(pipe_file, os.O_RDONLY)
while True:
    msg = os.read(fd_r, 1024)
    if msg == "":
        print "msg is none"
    elif msg == "quit":
        print "quit!"
        exit()
    print msg

