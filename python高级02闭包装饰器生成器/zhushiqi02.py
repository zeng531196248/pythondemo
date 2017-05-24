'''
注解方式使用装饰器,


'''
def test(func):
    print('-----1------')
    def inner():
        print('---权限可是验证----')
        func()
    return inner

@test
def f1():
    print("----f1---")

f1()
