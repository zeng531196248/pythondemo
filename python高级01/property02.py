'''
property第一种用法
'''

class Test(object):
    def __init__(self):
        self._num=100;

    @property
    def num(self):
        print('---get---')
        return self._num

    @num.setter
    def num(self,Nums):
        print('---set---')
        self._num=Nums




t=Test()
t.num=520
print(t.num)