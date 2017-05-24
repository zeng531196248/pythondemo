#conding=utf-8
import  copy
'''
    深层拷贝和浅拷贝
    浅拷贝只是一种引用
    深层拷贝，在拷贝值得基础上重新创建了对象


'''
a=[123,12,33]
b=a

c=a.copy()

print(b is a)#True
print( id(a))
print( c is a) #false
print(id (c))
