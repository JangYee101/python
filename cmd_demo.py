#!/usr/bin/python
#coding:utf-8
#不要用os.system和commands.getstatusoutput()来执行命令，因为可能会造成命令注入和资源浪费
import subprocess

#正确做法：参数化防止命令注入当命令如下时，不会创建aa文件，也不会执行ls -a命令
a = subprocess.Popen(['ls','-a;touch aa'])
print a.wait()
#错误做法：当执行如下命令时，会执行ls -a命令，也会创建bb文件
a = subprocess.Popen('ls -a;touch bb', shell=True)
print a.wait()

