#coding=gbk

"""
ģ��������������
"""

import sys
import socket
import threading
def middle(conn, addr):
    #�����������Socket
    sockDst = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockDst.connect((ipServer,portServer))
    while True:
        data = conn.recv(1024).encode()
        print('�ܵ��ͻ�����Ϣ��'+ data)
        if data == '��Ҫ����������':
            conn.send('����Ϣ�ѱ��������������'.encode())
            print('����Ϣ�ѹ���')
        elif data.lower() == 'bye':
            print(str(addr) + '�ͻ��˹ر�����')
            break
        else:
            sockDst.send(data.encode())
            print('��ת��������')
            data_fromServer = sockDst.recv(1024).decode()
            print('�յ��������ظ�����Ϣ��' + data_fromServer)
            if data_fromServer == '��Ҫ�����ͻ���':
                conn.send('����Ϣ�ѱ�����������޸�'.encode())
                print('��Ϣ�ѱ��۸�')
            else:
                conn.send(b'Server reply :'+data_fromServer.encode())
                print('��ת����������Ϣ���ͻ���')
    conn.close()
    sockDst.close()

def main():
    sockScr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockScr.bind(('',portScr))
    sockScr.listen(200)
    print('����������')
    while True:
        try:
            conn, addr = sockScr.accept()
            t = threading.Thread(target=middle,args=(conn, addr))
            t.start()
            print('�¿ͻ���'+ str(addr))
        except:
            pass

if __name__ == '__main__':
    try:
        #(����ip��ַ��portScr) <==> (ipServer��portServer)
        #��������������˿�
        portScr = int(sys.argv[1])
        #������ip��ַ��˿ں�
        ipServer =sys.argv[2]
        portServer = int(sys.argv[3])
        main()
    except:
        print('Sth error')