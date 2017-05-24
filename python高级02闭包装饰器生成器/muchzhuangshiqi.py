'''
多个装饰器进行装饰:
1.什么时候开始装饰：在python解释器开始读取时候已经开始装饰了

'''
def test(func):
    print('----装饰器1----')
    def inner1():
        print('--------b1---')
        func()
    return  inner1
def test2(func):
    print('----装饰器2----')
    def inner2():
        print('--------b2---')
        func()
    return  inner2
@test
@test2
def f1():
    print('--------函数1--')

f1()