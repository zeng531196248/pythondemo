'''
使用通用装饰器对函数进行日志打印

'''
def func(functionName):
    def func_in(*args, **kwargs):
        print("-----记录日志-----")
        ret = functionName(*args, **kwargs)
        return ret

    return func_in
@func
def f1():#无参数
    print("------------f1--------")
f1()
@func
def f2(a):#有参数
    print("-------f2-----a=%d"%a)
    return a*2 #并且有返回值的函数
ret=f2(4)
print(ret)
