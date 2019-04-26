#coding utf-8
# coding=gbk
# s = 'Hello world\n文本文件的读取方法\n文本文件的写入方法\n'
# with open('sample.txt','a+') as f:
#     f.write(s)

import os
# import os.path
# print(os.getcwd())

# import shutil
# shutil.make_archive('E:\\a','zip','E:\\Desktop','8')
# shutil.rmtree('E:\\a')

#查看CPU信息
import psutil
print(psutil.cpu_count())       #查看CPU核数
print(psutil.cpu_count(logical=False))      #查看物理CPU个数
print(psutil.cpu_percent())     #查看CPU使用率
print(psutil.cpu_percent(percpu=True))      #查看每个CPU的使用率
print(psutil.cpu_times())       #查看CPU时间分配情况

#查看开机时间
import datetime
t = psutil.boot_time()
print(datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S'))

#查看内存信息
virtual_memory = psutil.virtual_memory()
print(virtual_memory.total/1024/1024/1024)      #总内存大小
print(virtual_memory.used/1024/1024/1024)       #已使用内存
print(virtual_memory.free/1024/1024/1024)       #空闲内存
print(virtual_memory.percent)                   #内存使用率

#查看磁盘信息
print(psutil.disk_partitions())     #查看所有分区信息
print(psutil.disk_usage('C:\\'))    #查看指定分区的磁盘空间情况
print(psutil.disk_io_counters(perdisk=True))        #查看硬盘读写操作情况

#查看与网络连接有关的信息
print(psutil.net_connections())     #查看网络连接情况
print(psutil.net_io_counters())     #查看收发包情况
print(psutil.net_if_addrs())        #查看网络地址

#查看当前登陆用户信息
print(psutil.users())

#查看进程信息
print(psutil.pids())        #查看当前所有进程ID
p = psutil.Process(4204)    #获取指定ID的进程
print(p.name())             #进程名
print(p.username())         #查看创建该进程的用户名