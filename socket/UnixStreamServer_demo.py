#!/usr/bin/python
#coding:utf-8

import SocketServer
import os

class MyHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print self.request.recv(1024)
        self.request.send("welcome!!!")


addr_path = './unix.sock'
if os.path.exists(addr_path):
    os.remove(addr_path)
server = SocketServer.UnixStreamServer(addr_path, MyHandler)
server.serve_forever()
