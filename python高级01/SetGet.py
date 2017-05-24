#conding=utf-8
'''
set get 方法
私有化__
'''
class Test(object):
    def __init__(self):
        self.__num=100
    def setNum(self,setNum):
        self._num=setNum
    def getNum(self):
        return self._num


t=Test();
#print(t.__num)
print(t.__num)
print(t.getNum())
t.setNum(200)
print(t.getNum())

