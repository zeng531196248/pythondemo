#max() 和min()
#1.一般使用方法
temp=max(2,3,1)
print(temp)
#可迭代对象
a = [1, 2, 3, 4, 5, 6]
tmp = max(a)
print(tmp)
#key属性的使用，求出一组中绝对值最大的
a = [-9, -8, 1, 3, -4, 6]
tmp = max(a, key=lambda x: abs(x))
print(tmp)