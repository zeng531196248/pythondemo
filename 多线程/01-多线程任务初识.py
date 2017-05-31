'''
 主要的模块：from threading import Thread

'''
from threading import Thread
import  time

#定义一个函数
def test():
    print("----------泡妞我最爱------")
    time.sleep(1)

for i in range(5):
    Thread(target=test()).start()# 启动线程
