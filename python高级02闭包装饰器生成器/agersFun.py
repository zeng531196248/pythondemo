'''
    对有参数的构造函数进行装饰

'''
def test(func):
    print("-"*20)
    def inner(a,b):
        print("a=%d-----b=%d"%(a,b))#这里闭包内部的函数如果不加参数会报错
        func(a,b)#调用的函数同样也是这样
        print("---inner  end---")
    return  inner
@test
def f1(a,b):
    print("--f1---a=%d----b=%d"%(a,b))

f1(2,3)

