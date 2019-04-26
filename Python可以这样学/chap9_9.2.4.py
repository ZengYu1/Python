# coding=gbk
from time import sleep
from socket import gethostbyname
from datetime import datetime

def get_ipAddresses(url):
    ipAddresses = [0]
    while True:
        sleep(0.5)
        ip = gethostbyname(url)
        if ip != ipAddresses[-1]:      #目标主机IP地址发生变化
            ipAddresses.append(ip)
            print(str(datetime.now())[:19] + '===>' + ip)
            break

get_ipAddresses(r'www.baidu.com')
