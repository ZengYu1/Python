# coding=gbk

"""
ģ�����˴���
"""

import sys
import socket
import threading

#�ظ���Ϣ��ԭ������
def replyMessage(conn):
    while True:
        data = conn.recv(1024)
        conn.send(data)
        if data.encode().lower() == 'bye':
            break
    conn.close()

def main():
    sockScr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind(('', port))
    socket.listen(200)
    while True:
        try:
            conn, addr = socket.accept()
            #ֻ�����ض��������ʱ�������
            if addr[0] != onlyYou:
                conn.close()
                continue
            #�����������߳�
            t = threading.Thread(target=replyMessage, args=(conn,))
            t.start()
        except:
            print('error')

if __name__ == '__main__':
    try:
        #��ȡ�����в�����portΪ�����������˿�
        #ֻ����ip��ַΪonlyYou����������
        port = int(sys.argv[1])
        onlyYou = sys.argv[2]
        main()
    except:
        print('Must give me a munber as port')
