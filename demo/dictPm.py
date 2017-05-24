#字典的学习
#直接调用函数dict()
fdic=dict(([1,"y"],[2,"x"]))
print(fdic)
#调用函数fromkeys
#fromkeys(Keys,value)
#并不是一一对应。是多对一
#{1: ('x', 2, 3), 2: ('x', 2, 3), 3: ('x', 2, 3)}
fdics={}.fromkeys((1,2,3),("x",2,3))
print(fdics)
#当只有key时候
fdicNovalue={}.fromkeys((1,2))
print(fdicNovalue)
#{1: None, 2: None}
#访问字典中的值
dict2 = {'name': 'earth', 'port': 80}
for key in dict2.keys() :
    print("key=%s,value=%s"%(key,dict2[key]))
#key=name,value=earth key=port,value=80
#检测是否包含key
print("name" in dict2) #True
#python3 之前存在has_key()这个函数，但是现在被抛弃了
#更新字典
dict2['name']="1sss" #{'name': '1sss', 'port': 80}
print(dict2)
#删除
del dict2['name'] #删除单一的
del dict2 #删除所有的
dict2 .clear() #清空
dict2.pop("name")#删除并返回
#复制
dict2.copy()
#验证是否可以做key,返回hash值就可以做，
hash("name")
#返回一个包含字典中(键, 值)对元组的列表
dict2.items()
#  返回一个包含字典中所有值的列表
dict2.values()
#字典中部允许一个key对应多个值
dict3={2:2,1:"1"}
dict2.update(dict3)#可以把dict3加入dict2中，key重复的直接覆盖，不存在的直接添加
