# coding=gbk
import socket
#ʹ��ipv4Э�飬ʹ��UDP��������
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#�󶨶˿ںͶ˿ںţ����ַ�����ʾ�����κο���IP��ַ
s.bind(('',5000))
while True:
    data, addr = s.recvfrom(1024)
    #��ʾ���յ�������
    print('received message:{0} from PORT {1} on {2}'.format(data.decode(),
                                                             addr[1],addr[0]))
    if data.decode().lower() == 'bye':
        break
s.close()


