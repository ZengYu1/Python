#coding=gbk
"""
queueģ���Queue����ʵ���˶�������/�������߶���
ʹ��queue����ʵ���߳�ͬ��
"""
import threading
import time
import queue

#�Զ����������߳���
class Producer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        global myqueue
        #�ڶ���β��׷��Ԫ��
        myqueue.put(self.getName())
        print(self.getName(), ' put ', self.getName(), ' to queue.')

class Consumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        global myqueue
        #�ڶ����ײ���ȡԪ��
        print(self.getName(), ' get ', myqueue.get(), ' from queue')

myqueue = queue.Queue()

#�����������̺߳��������߳�
plist = []
clist = []
for i in range(10):
    p = Producer('Producer' + str(i))
    plist.append(p)
    c = Consumer('Consumer' + str(i))
    clist.append(c)

#���������������̺߳��������߳�
for p, c in zip(plist, clist):
    p.start()
    p.join()
    c.start()
    c.join()