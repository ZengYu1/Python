#coding=gbk
import threading
import time

#�Զ����߳���
class mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    #��дrun()����
    def run(self):
        global x
        #��ȡ��������ɹ�������ٽ���
        lock.acquire()
        x = x + 3
        print(x)
        #�˳��ٽ������ͷ���
        lock.release()

lock = threading.RLock()
#Ҳ����ʹ��Lock��ʵ�ּ������߳�ͬ��
#lock=threading.Lock()

#��Ŷ���̵߳��б�
t1 = []
for i in range(10):
    #�����̲߳���ӵ��б�
    t = mythread()
    t1.append(t)

#����̻߳�����ʵı���
x = 0
#�����б��е������߳�
for i in t1:
    i.start()