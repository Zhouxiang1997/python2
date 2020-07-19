# 如何创建字典
dictA={"pro":'艺术','shcool':'北京电影学院'} #空字典
# 添加字典数据
dictA['name']='李易峰'  #key:value
dictA['age']='30'
dictA['pos']='歌手'
#结束添加
# print(dictA) #输出完整的字典
# print(len(dictA))  #数据项长度
# print(type(dictA))

# print(dictA['name']) #通过键获取对应的值
# dictA['name']='谢霆锋'  #修改键对应的值
dictA['shcool']='香港大学'
# dictA.update({'height':1.80}) #可以添加或者更新
# print(dictA)

# 获取所有的键
# print(dictA.keys())
# 获取所有的值
# print(dictA.values())
# 获取所有的键和值
# print(dictA.items())
# for key,value in dictA.items():
#     print('%s==%s'%(key,value))

# 删除操作
# del dictA['name']  通过指定键进行删除
# dictA.pop('age')   通过指定键进行删除
print(dictA)
# 如何排序 按照key排序
# print(sorted(dictA.items(),key=lambda d:d[0]))
# 按照value排序
# print(sorted(dictA.items(),key=lambda d:d[1]))
# 字典拷贝
import copy
# dictB=copy.copy(dictA) #浅拷贝
dictC=copy.deepcopy(dictA) #深拷贝
print(id(dictC))
print(id(dictA))
# dictB['name']='peter'
dictC['name']='刘德华'
print(dictC)
print(dictA)
