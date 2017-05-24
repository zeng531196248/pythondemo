'''
property第一种用法
'''

class Test(object):
    def __init__(self):
        self._num=100;

    def setNum(self,Nums):
        print('---set---')
        self._num=Nums
    def getNum(self):
        print('---get---')
        return  self._num

    num=property(getNum,setNum)


t=Test()
t.num=520
print(t.num)