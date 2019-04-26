#coding=gbk
import threading
import time

#自定义线程类
class mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    #重写run()方法
    def run(self):
        global x
        #获取锁，如果成功则进入临界区
        lock.acquire()
        x = x + 3
        print(x)
        #退出临界区，释放锁
        lock.release()

lock = threading.RLock()
#也可以使用Lock类实现加锁和线程同步
#lock=threading.Lock()

#存放多个线程的列表
t1 = []
for i in range(10):
    #创建线程并添加到列表
    t = mythread()
    t1.append(t)

#多个线程互斥访问的变量
x = 0
#启动列表中的所有线程
for i in t1:
    i.start()