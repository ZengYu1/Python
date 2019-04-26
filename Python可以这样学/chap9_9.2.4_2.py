# coding=gbk
import socket
import nmap
nmScan = nmap.PortScanner()         #创建端口扫描对象
ip = socket.gethostbyname('www.baidu.com')     #获取目标主机的IP地址
nmScan.scan(ip,'80')        #扫描指定端口
print(nmScan[ip] ['tcp'] [80] ['state'])       #查看端口状态
