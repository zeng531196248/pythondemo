'''
互斥锁：
    A----》持有----》释放
    B----》等待----》持有-----》。。。







'''
from threading import Thread, Lock
import time

g_num=0
def testOne():
    global  g_num
    mutex.acquire()#一直等锁
    for i in range(1000000):
        g_num+=1
        print("------------One---g_num=%d"%g_num)
    mutex.release()#释放锁

def testTwo():
    global g_num
    mutex.acquire()  # 一直等锁
    for i in range(1000000):
        g_num += 1
        print("------------Two---g_num=%d" % g_num)
    mutex.release()  # 释放锁


#创建一把互斥锁，这个锁默认是没有上锁的
mutex = Lock()

Thread(target=testTwo).start()
Thread(target=testOne).start()



