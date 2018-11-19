#!/usr/bin/env python
#coding:utf-8
import logging
#CRITICAL > ERROR > WARNING > INFO > DEBUG
#critical > error > warning > info > debug
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
    datefmt = '%a, %d %b %Y %H:%M:%S',
    #filename = '/tmp/JY/test.log',
    filename = '',
    filemode = 'a')
try:
    print asdfas
except:
    logging.error("this is my logging recode error!")
    logging.exception("显示详细错误信息和行数")
