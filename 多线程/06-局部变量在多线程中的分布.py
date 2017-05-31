'''
多线程中,全局变量存在共享,
但是局部变量会被拷贝相同一份,不会有影响

结果：
----thread name is Thread-1 ----
--thread is Thread-1----g_num=101
----thread name is Thread-2 ----
----thread name is Thread-3 ----
--thread is Thread-2----g_num=100
--thread is Thread-3----g_num=100

线程1：101 对后面的线程并没有产生影响




'''

from threading import Thread
import threading
import time

def  test():
    name=threading.current_thread().name
    print("----thread name is %s ----" % name)
    g_num = 100
    if name == "Thread-1":
        g_num += 1
    else:
        time.sleep(2)
    print("--thread is %s----g_num=%d" % (name, g_num))



Thread(target=test).start()
Thread(target=test).start()
Thread(target=test).start()