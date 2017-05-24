'''
    Python 闭包 基础
    最简单的闭包

'''

def test(num):
    print('-----1------')
    def innertest(num2):
        print('----------inner----')
        print(num+num2)
    print('------2-------')
    return  innertest

inner=test(250)
inner(520)