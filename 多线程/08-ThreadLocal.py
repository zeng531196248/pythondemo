'''
ThreadLocal:线程变量,和java差不多
报错：threading.Thread(target=process_thread,args=('zz',),name='AA').start()

其实这句话在如参数时候要主要args=('zz',)这个后面一定要偶,隔开.

'''
import  threading
thread_A=threading.local()

def display():
    aname=thread_A.name
    print('Hello, %s (in %s)' % (aname, threading.current_thread().name))

def process_thread(name):
    thread_A.name=name
    display()

threading.Thread(target=process_thread,args=('zz',),name='AA').start()
threading.Thread(target=process_thread,args=('zzz',),name='CC').start()
