#coding=gbk
"""
ģ��ͻ��˴���
"""

import sys
import socket

def main():
    socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.connect((ip, port))
    while True:
        data = input('what do you want to ask:')
        sock.send(data.encode())
        print(sock.recv(1024).decode())
        if data.lower() == 'bye':
            break
    sock.close()

if __name__ == '__main__':
    try:
        #�����������ip��ַ�Ͷ˿ں�
        ip = sys.argv[1]
        port = int(sys.argv[2])
        main()
    except:
        print('Sth error')