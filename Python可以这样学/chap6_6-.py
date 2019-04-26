#coding utf-8
# coding=gbk
# s = 'Hello world\n�ı��ļ��Ķ�ȡ����\n�ı��ļ���д�뷽��\n'
# with open('sample.txt','a+') as f:
#     f.write(s)

import os
# import os.path
# print(os.getcwd())

# import shutil
# shutil.make_archive('E:\\a','zip','E:\\Desktop','8')
# shutil.rmtree('E:\\a')

#�鿴CPU��Ϣ
import psutil
print(psutil.cpu_count())       #�鿴CPU����
print(psutil.cpu_count(logical=False))      #�鿴����CPU����
print(psutil.cpu_percent())     #�鿴CPUʹ����
print(psutil.cpu_percent(percpu=True))      #�鿴ÿ��CPU��ʹ����
print(psutil.cpu_times())       #�鿴CPUʱ��������

#�鿴����ʱ��
import datetime
t = psutil.boot_time()
print(datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S'))

#�鿴�ڴ���Ϣ
virtual_memory = psutil.virtual_memory()
print(virtual_memory.total/1024/1024/1024)      #���ڴ��С
print(virtual_memory.used/1024/1024/1024)       #��ʹ���ڴ�
print(virtual_memory.free/1024/1024/1024)       #�����ڴ�
print(virtual_memory.percent)                   #�ڴ�ʹ����

#�鿴������Ϣ
print(psutil.disk_partitions())     #�鿴���з�����Ϣ
print(psutil.disk_usage('C:\\'))    #�鿴ָ�������Ĵ��̿ռ����
print(psutil.disk_io_counters(perdisk=True))        #�鿴Ӳ�̶�д�������

#�鿴�����������йص���Ϣ
print(psutil.net_connections())     #�鿴�����������
print(psutil.net_io_counters())     #�鿴�շ������
print(psutil.net_if_addrs())        #�鿴�����ַ

#�鿴��ǰ��½�û���Ϣ
print(psutil.users())

#�鿴������Ϣ
print(psutil.pids())        #�鿴��ǰ���н���ID
p = psutil.Process(4204)    #��ȡָ��ID�Ľ���
print(p.name())             #������
print(p.username())         #�鿴�����ý��̵��û���