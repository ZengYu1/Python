# coding=gbk
"""
网络嗅探器程序可以检测本机所在局域网内的流量和数据包收发情况，对于网络管理具有重要作用
也属于系统运维内容之一，为了实现网络流量嗅探，需要将网卡设置为混杂模式，并且运行嗅探器程序的用户账号需要拥有系统管理员权限
下面的代码运行60s，然后输出本机所在局域网内飞奔及发出的数据包，并统计不同主机发出
的数据包数量。
"""
import socket
import threading
import time

activeDegree = dict()
flag = 1
def main():
    global activeDegree
    global flag
    #获取本机IP地址
    HOST = socket.gethostbyname(socket.gethostname())
    #创建原始套接字，适用于Windows平台
    #对于其他操作系统，要把socket.IPPROTO_IP替换为socket.IPPROTO_ICMP
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((HOST, 0))
    #启用混杂模式，捕捉所有数据包
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    #开始捕捉数据包
    while flag:
        c = s.recvfrom(65565)
        host = c[1][0]
        activeDegree[host] = activeDegree.get(host,0)+1
        if c[1][0] != '192.168.37.2':
            print(c)
    #关闭混杂模式
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    s.close()
t = threading.Thread(target=main)
t.start()
time.sleep(60)
flag = 0
t.join()
for item in activeDegree.items():
    print(item)

