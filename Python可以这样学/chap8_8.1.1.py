# coding=gbk
import sqlite3
import hashlib

#�Զ��庯��
def md5sum(t):
    return hashlib.md5(t).hexdigest()

#���ڴ��д�����ʱ���ݿ�
conn = sqlite3.connect(":memory:")
#��������SQL�е��õĺ���
conn.create_function("md5", 1, md5sum)
cur = conn.cursor()
#��SQL����е����Զ��庯��
cur.execute("SELECT md5(?)",["�й�ɽ����̨".encode()])
print(cur.fetchone()[0])