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