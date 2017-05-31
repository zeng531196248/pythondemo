'''
多线程进行使用全局变量出现的问题:
按照预先设计的应该会不对，但是这里我测试几次发现结果都是正常的，这部不符合

'''
import  time
from threading import Thread
import  os
#定义一个全局变量
g_num=0
def testOne():
    global  g_num
    for i in range(1000000):
        g_num+=1
        print("------------One---g_num=%d"%g_num)


def testTwo():
    global g_num
    for i in range(1000000):
        g_num += 1
        print("------------Two---g_num=%d" % g_num)

Thread(target=testOne()).start()
#time.sleep(1)
Thread(target=testTwo()).start()
print(g_num)
Thread(target=testTwo()).start()
Thread(target=testTwo()).start()