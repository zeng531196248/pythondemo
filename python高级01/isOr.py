#conding=utf-8
'''
    is 和 == 的区别
    ==比较的是值相等
    is比较的是内存地址


'''

a =123
b=123
print(a==b)#True

c=a
print(c is b)#True

e=[1,2,3]
f=[1,2,3]
print(e==f)#True
print(e is f) #false
