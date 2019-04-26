#coding=gbk
import socket
import sys
import re
import struct
import getpass

def main(serverIP):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((serverIP,10600))
    userId = input('�������û�����')
    #ʹ��getpassģ���getpass()������ȡ���룬������
    userPwd = getpass.getpass('���������룺')
    message = userId + ',' + userPwd
    sock.send(message.encode())
    login = sock.recv(100)
    #��֤�Ƿ��½�ɹ�
    if login == b'error':
        print('�û������������')
        return
    #���������С
    intSize = struct.calcsize('I')
    while True:
        #���ܿͻ����������##>����ʾ��
        command = input('##>').lower().strip()
        #û�������κ���Ч�ַ�����ǰ������һ��ѭ�����ȴ��û���������
        if not command:
            continue
        #�����˷�������
        command = ''.join(command.split())
        sock.send(command.encode())
        #�˳�
        if command in ('quit','q'):
            break
        #�鿴�ļ��б�
        elif command in ('list','ls','dir'):
            #�Ƚ����ַ�����С���ٸ���������պ����������ַ���
            loc_size = struct.unpack('I', sock.recv(intSize))[0]
            files = eval(sock.recv(loc_size).decode())
            for item in files:
                print(item)
        #�л�����һ��Ŀ¼
        elif ''.join(command.split()) == 'cd..':
            print(sock.recv(100).decode())
        #�鿴��ǰ����Ŀ¼
        elif command in ('cwd','cd'):
            print(sock.recv(1024).decode())
        #�л������ļ���
        elif command.startswith('cd '):
            print(sock.recv(100).decode())
        #�ӷ����������ļ�
        elif command.startswith('get '):
            isFileExit = sock.recv(20)
            #�ļ�������
            if isFileExit != b'ok':
                print('error')
            #�ļ����ڣ���ʼ����
            else:
                print('downloading.',end='')
                fp = open(command.split()[1],'wb')
                while True:
                    #��ʾ����
                    print('.',end='')
                    data = sock.recv(4096)
                    if data == b'overxxxx':
                        break
                    fp.write(data)
                    sock.send(b'ok')
                fp.close()
                print('ok')
        #��Ч����
        else:
            print('��Ч����')
    sock.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:{0} serverIPAddress'.format(sys.argv[0]))
        exit()
    serverIP = sys.argv[1]
    #ʹ��������ʽ�жϷ�������ַ�Ƿ�Ϊ�Ϸ���IP��ַ
    if re.match(r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$',serverIP):
        main(serverIP)
    else:
        print('��������ַ���Ϸ�')
        exit()


