'''
带有参数的装饰器
'''
def fun_arges(arg):
    def test(func):
        print("----装饰器-----")
        def inner():
            print("---------innner----")
            if arg=="1":
                func()
                func()
            else:
                func
        return inner #返回内部调用的闭包
    return test#返回外包
@fun_arges("1")
def test():
    print("--test--")

#带有参数的装饰器,能够起到在运行时,有不同的功能
@fun_arges("haha")
def test2():
    print("--test2--")

test()
test2()
