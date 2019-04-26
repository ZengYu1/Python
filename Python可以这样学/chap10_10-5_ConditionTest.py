#coding=gbk
"""
ʹ��Condition���������ĳЩ�¼�������Ŵ������ݻ�ִ���ض��Ĺ��ܴ��룬�������ڲ�ͬ�߳�֮���ͨ�Ż�
֪ͨ����ʵ�ָ��߼����ͬ����
����ͨ�������������/��������������ʾCondition������÷���
�������̺߳��������̹߳���һ���б������߸������б�β��׷��Ԫ�أ�����������б��ײ���ȡ��ɾ��Ԫ�أ�
����б��ȵ���20��ʾ�����������ߵȴ�������б��ѿ��������ߵȴ�
"""

import threading
from random import randint
from time import sleep

#�Զ����������߳���
class Producer(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
        global x
        while True:
            #��ȡ��
            con.acquire()
            #���蹲���б������������20��Ԫ��
            if len(x) == 20:
                #��������б������������ߵȴ�
                con.wait()
                print('Producer is waiting����')
            else:
                print('Producer:', end=' ')
                #������Ԫ�أ�����������б�
                x.append(randint(1,1000))
                print(x)
                sleep(1)
                #����ȴ��������߳�
                con.notify()
            #�ͷ���
            con.release()

#�Զ����������߳���
class Consumer(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
        global x
        while True:
            #��ȡ��
            con.acquire()
            if not x:
                #�ȴ�
                con.wait()
                print('Consumer is waiting����')
            else:
                print(x.pop(0))
                print(x)
                sleep(2)
                con.notify()
            con.release()

#����Condition�����Լ��������̺߳��������߳�
con = threading.Condition()
x= []
p = Producer('Producer')
c = Consumer('Consumer')
p.start()
c.start()
p.join()
c.join()
