#coding=gbk

"""
����˴���
"""

import socket
import threading
import os
import struct

## �û��˺š����롢��Ŀ¼
#Ҳ���԰���Щ��Ϣ��������ݿ���
users = {'zhangsan':{'pwd':'zhangsan1234','home':r'e:\python 3.6'},
         'lisi':{'pwd':'lisi5678','home':'e:\\'}}

def server(conn, addr, home):
    print('�¿ͻ��ˣ�' + str(addr))
    #���뵱ǰ�û���Ŀ¼
    os.chdir(home)
    while True:
        data = conn.recv(100).decode().lower
        #��ʾ�ͻ��������ÿһ������
        print(data)
        #�ͻ����˳�
        if data in ('quit','q'):
            break
        #�鿴��ǰ�ļ��е��ļ��б�
        elif data in ('list','ls','dir'):
            files = str(os.listdir(os.getcwd()))
            files = files.encode()
            #�ȷ����ֽڴ���С���ٷ����ֽڴ�
            conn.send(struct.pack('I',len(files)))
            conn.send(files)
        #�л�����һ��Ŀ¼
        elif ''.join(data.split()) == 'cd..':
            cwd = os.getcwd()
            newCwd = cwd[:cwd.rindex('\\')]
            #���Ǹ�Ŀ¼�����
            if newCwd[-1] == ':':
                newCwd += '\\'
            #�޶��û���Ŀ¼
            if newCwd.lower().startswith(home):
                os.chdir(newCwd)
                conn.send(b'ok')
            else:
                conn.send(b'error')
        #�鿴��ǰĿ¼
        elif data in ('cwd', 'cd'):
            conn.send(str(os.getcwd()).encode())
        elif data.startswith('cd'):
            #ָ�����ָ�����������Ŀ���ļ��д��пո�����
            #ֻ����ʹ�����·��������ת
            data = data.split(maxsplit = 1)
            if len(data) == 2 and os.path.isdir(data[1]) and data[1] != os.path.abspath(data[1]):
                os.chdir(data[1])
                conn.send(b'ok')
            else:
                conn.send(b'error')
        #�����ļ�
        elif data.startswith('get '):
            data = data.split(maxsplit = 1)
            #����ļ��Ƿ����
            if len(data) == 2 and os.path.isfile(data[1]):
                conn.send(b'ok')
                fp = open(data[1], 'rb')
                while True:
                    content = fp.read(4096)
                    #�����ļ�����
                    if not content:
                        conn.send(b'overxxxx')
                        break
                    #�����ļ�����
                    conn.send(content)
                    if conn.recv(10) == b'ok':
                        continue
                fp.close()
            else:
                conn.send(b'no')
        #��Ч����
        else:
            pass

    conn.close()
    print(str(addr) + '�ر�����')

#����Socket���������ض˿ڣ��ȴ��ͻ�������
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',10600))
sock.listen(5)
while True:
    conn,addr = sock.accept()
    #��֤�ͻ���������û����������Ƿ���ȷ
    userId, userPwd =conn.recv(1024).encode().split(',')
    if userId in users and users[userId]['pwd'] == userPwd:
        conn.send(b'ok')
        #Ϊÿ���ͻ������Ӵ���������һ���߳�
        #����Ϊ���ӡ��ͻ��˵�ַ���ͻ���Ŀ¼
        home = users[userId]['home']
        t = threading.Thread(target=server, args=(conn,addr,home))
        t.daemon = True
        t.start()
    else:
        conn.send(b'error')