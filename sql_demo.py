#!/usr/bin/python
#coding:utf-8

import MySQLdb

#链接数据库
db = MySQLdb.connect('localhost', 'root', 'password', 'the_DB', charset='utf8')
#获取游标
cursor = db.cursor()

sql_str = "select * from the_table where id = %s"

opt = '1 or 1=1'#用户恶意输入，简单的sql注入

#错误方法：将查询出所有表内数据
cursor.execute(sql_str % opt)

#正确方法：使用参数化，防止sql注入
cursor.execute(sql_str, opt)





