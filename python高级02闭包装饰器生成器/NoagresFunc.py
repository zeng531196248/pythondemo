'''
使用装饰器对无参数的构造函数进行装饰
'''
def test(func):
    print("--------test--------")
    def inner():
        print('-----inner-------')
        func()
    return  inner
@test
def f1():
    print('==f1===')
f1()