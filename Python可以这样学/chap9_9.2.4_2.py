# coding=gbk
import socket
import nmap
nmScan = nmap.PortScanner()         #�����˿�ɨ�����
ip = socket.gethostbyname('www.baidu.com')     #��ȡĿ��������IP��ַ
nmScan.scan(ip,'80')        #ɨ��ָ���˿�
print(nmScan[ip] ['tcp'] [80] ['state'])       #�鿴�˿�״̬
