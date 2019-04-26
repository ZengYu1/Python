#coding=gbk
"""
使用Condition对象可以在某些事件触发后才处理数据或执行特定的功能代码，可以用于不同线程之间的通信或
通知，以实现更高级别的同步。
下面通过经典的生产者/消费者问题来演示Condition对象的用法：
生产者线程和消费者线程共享一个列表，生产者负责在列表尾部追加元素，消费者则从列表首部获取并删除元素，
如果列表长度到了20表示已满，生产者等待，如果列表已空则消费者等待
"""

import threading
from random import randint
from time import sleep

#自定义生产者线程类
class Producer(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
        global x
        while True:
            #获取锁
            con.acquire()
            #假设共享列表中最多能容纳20个元素
            if len(x) == 20:
                #如果共享列表已满，生产者等待
                con.wait()
                print('Producer is waiting……')
            else:
                print('Producer:', end=' ')
                #产生新元素，添加至共享列表
                x.append(randint(1,1000))
                print(x)
                sleep(1)
                #幻想等待条件的线程
                con.notify()
            #释放锁
            con.release()

#自定义消费者线程类
class Consumer(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
        global x
        while True:
            #获取锁
            con.acquire()
            if not x:
                #等待
                con.wait()
                print('Consumer is waiting……')
            else:
                print(x.pop(0))
                print(x)
                sleep(2)
                con.notify()
            con.release()

#创建Condition对象以及生产者线程和消费者线程
con = threading.Condition()
x= []
p = Producer('Producer')
c = Consumer('Consumer')
p.start()
c.start()
p.join()
c.join()
