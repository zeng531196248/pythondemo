#reduce()函数
from functools import reduce
def f(x,y):
    return  x+y

print(reduce(f, [1, 3, 5, 7, 9]))
# 先计算头两个元素：f(1, 3)，结果为4；
# 再把结果和第3个元素计算：f(4, 5)，结果为9；
# 再把结果和第4个元素计算：f(9, 7)，结果为16；
# 再把结果和第5个元素计算：f(16, 9)，结果为25；
# 由于没有更多的元素了，计算结束，返回结果25。
# 类似于求和

reduce(f, [1, 3, 5, 7, 9], 100)
#125
#因为起始是（100+1）开始进行计算



