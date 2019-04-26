import sqlite3
cn.sqlite3.connect('plan.dat')
sql = "create table data(专业代码 text,专业名称 text,层次 text，科类 text,学制 text,收费标准 int)"
cn.execute(sql)