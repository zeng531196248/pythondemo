'''
对有返回值的闭包进行装饰

'''
def test(func):
    print("-"*20)
    def inner(*agrs,**kwargs):
        res= func(*agrs,**kwargs)#保存返回值
        print("---inner  end---")
        return res#返回函数已经调用的并且返回了结果
    return  inner
@test
def f1(a,b,c):
    print("--f1---a=%d----b=%d---c=%d"%(a,b,c))
    return a+b+c

res=f1(2,3,4)
print(res)