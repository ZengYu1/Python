#coding=gbk
"""
queue模块的Queue对象实现了多生产者/多消费者队列
使用queue对象实现线程同步
"""
import threading
import time
import queue

#自定义生产者线程类
class Producer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        global myqueue
        #在队列尾部追加元素
        myqueue.put(self.getName())
        print(self.getName(), ' put ', self.getName(), ' to queue.')

class Consumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        global myqueue
        #在队列首部获取元素
        print(self.getName(), ' get ', myqueue.get(), ' from queue')

myqueue = queue.Queue()

#创建生产者线程和消费者线程
plist = []
clist = []
for i in range(10):
    p = Producer('Producer' + str(i))
    plist.append(p)
    c = Consumer('Consumer' + str(i))
    clist.append(c)

#依次启动生产者线程和消费者线程
for p, c in zip(plist, clist):
    p.start()
    p.join()
    c.start()
    c.join()