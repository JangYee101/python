#!/usr/bin/python
#coding:utf-8

import socket

sock = socket.socket()
host = '127.0.0.1'
port = 12345
sock.bind((host, port))
sock.listen(5)
clie, addr = sock.accept()
print '连接地址：', addr
print '消息：', clie.recv(1024)
clie.send('welcome!!!')
clie.close()
sock.close()
