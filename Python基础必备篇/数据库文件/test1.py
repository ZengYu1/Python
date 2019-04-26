#coding=utf8

import pymysql

#创建数据库连接
connection = pymysql.connect("192.168.199.146","root","111111","test1")

#创建cursor
cursor =connection.cursor()
sql="select * from t_account"

#cursor 执行sql
cursor.execute(sql)

#获取cursor执行之后第一行结果
emp=cursor.fetchone()
print(type(emp))
print(emp)

#关闭游标
cursor.close()
connection.close()