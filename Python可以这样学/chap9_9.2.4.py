# coding=gbk
from time import sleep
from socket import gethostbyname
from datetime import datetime

def get_ipAddresses(url):
    ipAddresses = [0]
    while True:
        sleep(0.5)
        ip = gethostbyname(url)
        if ip != ipAddresses[-1]:      #Ŀ������IP��ַ�����仯
            ipAddresses.append(ip)
            print(str(datetime.now())[:19] + '===>' + ip)
            break

get_ipAddresses(r'www.baidu.com')
