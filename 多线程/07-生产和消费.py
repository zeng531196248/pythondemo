'''
生产和消费：使用队列

'''

#encoding=utf-8
import threading
import time

#python2中
#from Queue import Queue

#python3中
from queue import Queue


#生产者
class Pro(threading.Thread):
    def run(self):
        global  queue
        count=0
        while True:
            if  queue.qsize() < 1000:
                for i in range(100):
                    count = count +1
                    msg = '生成产品'+str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

#消费者
class Cons(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + '消费了 ' + queue.get()
                    print(msg)
            time.sleep(1)

if __name__=="__main__":
    queue=Queue()#生成队列
    #初始化生产
    for i in range(500):
        queue.put('初始产品'+str(i))
    for i in range (2):
        Pro().start()

    for i in range(5):
        Cons().start()


