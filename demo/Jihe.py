#集合本身是无序的
#可变集合set 和不可变集合frozenset
#可变集合set可以进行编辑删除，不可以变集合frozenset不行
s=set("apdsadsajijo")
print(s)#{'i', 'd', 'p', 'j', 's', 'a', 'o'} 打印结果
m=frozenset("apdsadsajijo")
print(m)#frozenset({'i', 'j', 's', 'p', 'o', 'a', 'd'})
for i in  s :
    print(i)
for x in  m :
    print(x)
print(type(m))#frozenset
print(type(s))#set
print(m==s) #true
s.add("ss")#更新集合
print(s)#{'a', 'o', 'j', 'ss', 'p', 'i', 'd', 's'}
s.update("kl")#update 也是添加 存在的就不添加。并不存在的就添加
print(s)#{'a', 'j', 'd', 's', 'ss', 'l', 'p', 'k', 'o', 'i'}
s-=set("kl")#移除
print(s)#{'a', 'j', 'd', 's', 'ss', 'p', 'o', 'i'}
s.remove("o")#移除
print(s)#{'a', 'j', 'd', 's', 'ss', 'p', 'i'}
del s #删除
#集合的比较
#集合的比较只有当一个集合中得延元素和另外一个集合中得元素相同时候
bset=set("abc")
cset=set("abc")
print(id(bset))#54380104
print(id(cset))#54380704
print(bset==cset)#True
#子集和父集比较
dset=set("qwer")
eset=set("qwertyu")
print(dset<=eset)#True
#联合
fset=dset | eset
print(fset) #{'w', 'u', 'y', 'q', 't', 'r', 'e'} 合并的都是不重复的
#交集
print(dset&eset)#{'q', 'w', 'r', 'e'}
#
eset &= set("abct")
print(eset) #{'t'} &=并集后在赋值
# s.issubset(t) 如果 s 是 t 的子集，则返回 True,否则返回 False
# s.issuperset(t) 如果 t 是 s 的超集，则返回 True,否则返回 False
# s.union(t) 返回一个新集合，该集合是 s 和 t 的并集
# s.intersection(t) 返回一个新集合，该集合是 s 和 t 的交集
# s.difference(t) 返回一个新集合，该集合是 s 的成员，但不是 t 的成员
# s.symmetric_difference(t) 返回一个新集合，该集合是 s 或 t 的成员，但不是 s 和 t 共有的
# 成员
# s.copy() 返回一个新集合，它是集合 s 的浅复制

#以上方法都是只适合可变集合

# s.discard(obj) 如果 obj 是集合 s 中的元素，从集合 s 中删除对象 obj

