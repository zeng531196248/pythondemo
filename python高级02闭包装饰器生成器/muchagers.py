'''
装饰器对不定长度的构造函数进行装饰

'''

def test(func):
    print("-"*20)
    def inner(*agrs,**kwargs):
        func(*agrs,**kwargs)#调用的函数同样也是这样
        print("---inner  end---")
    return  inner
@test
def f1(a,b,c):
    print("--f1---a=%d----b=%d---c=%d"%(a,b,c))

f1(2,3,4)


