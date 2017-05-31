'''对线程进行传参数
书写代码中出现的错误：
 print("-----------agrs",agrss)#正确

 print("-----------agrs"+agrss)#错误---习惯性的java写法不行

返回结果：
    ----testInNumOne---
    -----------agrs [11, 22, 33, 44]
    ----testInNumTwo---
    -----------agrs [11, 22, 33, 44]


    可以看出：当我们改变全局共享变量时候，其他线程在操作这个共享变量时候也是可以使用的
    也看出了全局变量的不安全，容易被其他线程改变


'''
from threading import Thread
import time

def testInNumOne(agrss):
    print("----testInNumOne---")
    agrss.append(44)
    print("-----------agrs",agrss)#


def testInNumTwo(agrss):
    time.sleep(1)
    print("----testInNumTwo---")
    print("-----------agrs",agrss)

agrss= [11,22,33]

Thread(target=testInNumOne,args=(agrss,)).start()

Thread(target=testInNumTwo,args=(agrss,)).start()

