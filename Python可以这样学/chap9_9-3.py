# coding=gbk
"""
������̽��������Լ�Ȿ�����ھ������ڵ����������ݰ��շ����������������������Ҫ����
Ҳ����ϵͳ��ά����֮һ��Ϊ��ʵ������������̽����Ҫ����������Ϊ����ģʽ������������̽��������û��˺���Ҫӵ��ϵͳ����ԱȨ��
����Ĵ�������60s��Ȼ������������ھ������ڷɱ������������ݰ�����ͳ�Ʋ�ͬ��������
�����ݰ�������
"""
import socket
import threading
import time

activeDegree = dict()
flag = 1
def main():
    global activeDegree
    global flag
    #��ȡ����IP��ַ
    HOST = socket.gethostbyname(socket.gethostname())
    #����ԭʼ�׽��֣�������Windowsƽ̨
    #������������ϵͳ��Ҫ��socket.IPPROTO_IP�滻Ϊsocket.IPPROTO_ICMP
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((HOST, 0))
    #���û���ģʽ����׽�������ݰ�
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    #��ʼ��׽���ݰ�
    while flag:
        c = s.recvfrom(65565)
        host = c[1][0]
        activeDegree[host] = activeDegree.get(host,0)+1
        if c[1][0] != '192.168.37.2':
            print(c)
    #�رջ���ģʽ
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    s.close()
t = threading.Thread(target=main)
t.start()
time.sleep(60)
flag = 0
t.join()
for item in activeDegree.items():
    print(item)

