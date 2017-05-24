#coding-utf8
# 1.题目1
# 给一个字符串，统计其中的数字、字母和其他类型字符的个数；
# 比如输入“124mid-=”，输出：数字=3，字母=3，其他=2。

#--------------------------------例子----------------------
# s=input("请输入..")
# print(s.isdigit())  # 用isdigit函数判断是否数字
# print(s.isalpha())  # isalpha判断是否字母
# print(not (s.isalpha() or s.isdigit()) and s.isalnum())  # isalnum判断是否数字和字母的组合

#----------------------------------------end----------------------------

#定义初始化变量
# strcount=0
# intcount=0
# othercount=0
# s=input("请输入..")
# for i in  s :
#     if i.isdigit() :
#         intcount+=1
#     elif i.isalpha() :
#         strcount+=1
#     else:
#         othercount+=1
# print("字母=%d,数字=%d,其他的=%d"%(strcount,intcount,othercount))

#---------------------------------------------------end---------------------
# 题目2：删除列表中重复的元素
# 如果列表中有重复的元素，我们想要删除重复的
# li = [1, 2, 3, 4, 5, 2, 1, 3, 4, 57, 8, 8, 9]
# print(li)#打印下
# for x in  li :
#      while li.count(x) > 1 :
#          li.remove(x)
#
# print(li)

#-----------------------------------------end-----------------
#给定一个数，判断其是否为素数
#素数就是只能被自己和他的本身整除

# while True :
#    num = input("判断素数小能手,请输入...")
#    if num < 2 :
#        print  "this number is not a prime"
#
#        continue
#    i = 2
#    while i < num:
#        if num % i == 0:
#            print
#            "this number is not a prime"
#            break
#        i = i + 1
#    if i >= num:
#        print
#        "%d is a prime" % (num)
# 题目4
# 5-3 标准类型运算符. 写一段脚本，输入一个测验成绩，根据下面的标准，输出他的评分
# 成绩（A-F）。
# A: 90–100
# B: 80–89
# C: 70–79
# D: 60–69
# F: <60
# while True :
#     num=input("请输入查询的成绩...")
#     num=int(num)
#     if num > 90 and num <100 :
#         print("A")
#     elif num > 80 and num <89 :
#         print("B")
#     elif num > 70 and num <79 :
#         print("C")
#     elif num > 60 and num <69 :
#         print("D")
#     else:
#         print("F")
#
# --------------------------------------------end-----------------------
# 6–1. 字符串.string 模块中是否有一种字符串方法或者函数可以帮我鉴定一下一个字符串
# 是否是另一个大字符串的一部分?
# 使用in 或者 not in 来进行判断
#-------------------------end-------------------------------------------
# -------------------------end-------------------------------------------\
#     排序
# (a) 输入一串数字,从大到小排列之.
# 对元祖的形式
# num=(22,2,1,4,55)
# num=sorted(num)
# print(num)
# 对列表的形式
# numlist=[222,1,223,2]
# numlist.sort();
# print(numlist)

# (b) 跟 a 一样,不过要用字典序从大到小排列之.
# numdic = {11:"a",20:"H",-1:"K",5:"o"}
# print(sorted(numdic))
#-----------------------------------end---------------
# 字符串.创建一个 string.strip()的替代函数:接受一个字符串,去掉它前面和后面的
# 空格(如果使用 string.*strip()函数那本练习就没有意义了)


# ----------------------------------------------------------
# 6–12.字符串
# (a)创建一个名字为 findchr()的函数,函数声明如下:
# def findchr(string, char)
# findchr()要在字符串 string 中查找字符 char,找到就返回该值的索引,否则返回-1.不能用
# string.*find()或者 string.*index()函数和方法
# (b)创建另一个叫 rfindchr()的函数,查找字符 char 最后一次出现的位置.它跟 findchr()工作
# 类似,不过它是从字符串的最后开始向前查找的.
# (c)创建第三个函数,名字叫 subchr(),声明如下:
# def subchr(string, origchar, newchar)
# subchr()跟 findchr()类似,不同的是,如果找到匹配的字符就用新的字符替换原先字符.返回
# 修改后的字符串
#这个写法或导致返回不彻底
# def findchr( string, char ):
#     i=0
#     for x in string :
#         if x==char :
#             return i
#         i += 1
#     return -1
# num=findchr("shdsaldh",'f')
# print(num)
# ------------2----------
# def rfindchr( string, char ):
#     i=-1
#     x=0;
#     length = len(string)
#     while x < length :
#         if char == string[i] :
#             return  length+i
#         x+=1
#         i=i+-1
# num=rfindchr("shdsaldh",'d')
# print(num)
# -------------3----------------
# def  subchr(string, origchar, newchar) :
#     length=len(string)
#     x = 0
#     while x < length :
#         if origchar == string[x] :
#             string[x] = newchar
#         x+=1
#     return string
# sts=subchr("shdsaldh",'d','N')
# print(sts)
#-------------------end----------------
# 方法.实现一个叫 myPop()的函数,功能类似于列表的 pop()方法,用一个列表作为输入,
# 移除列表的最新一个元素,并返回它.
# def myPop( lists) :
#     x = lists[0]
#     del  lists[0]
#     return x
# lists = [2,3,4,1,2]
# print(myPop(lists))
#--------------------------------end----------------------



