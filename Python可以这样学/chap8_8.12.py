# coding=gbk
import sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE people(name_last,age)")
who = "Dong"
age = 38
#ʹ���ʺ���Ϊռλ��
cur.execute("INSERT INTO people VALUES(?,?)",(who,age))
#ʹ������������Ϊռλ��
cur.execute("SELECT * FROM people WHERE name_last = :who AND age=:age",
            {"who":who,"age":age})
print(cur.fetchone()) 