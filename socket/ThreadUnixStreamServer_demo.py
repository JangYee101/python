#!/usr/bin/python
#coding:utf-8

import SocketServer
import os
import threading
import time

thread_lock_100 = threading.Semaphore(1)

class MyHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print self.request.recv(1024)
        #self.request.send("welcome!!!")
        thread_lock_100.acquire()
        time.sleep(10)
        with open('./myre.txt','a') as fd:
            fd.write('aaa')
        thread_lock_100.release()


addr_path = './unix.sock'
if os.path.exists(addr_path):
    os.remove(addr_path)
#server = SocketServer.UnixStreamServer(addr_path, MyHandler)
server = SocketServer.ThreadingUnixStreamServer(addr_path, MyHandler)
server.serve_forever()
