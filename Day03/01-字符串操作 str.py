# 字符串常用
capitalize()                     # 首字母变大写
endswith/startswith()            # 是否 x结束/开始
find()                           # 检测x是否在字符串中
isalnum()                        # 判断是否是字母和数字
isalpha()                        # 判断是否是字母
isdigit()                        # 判断是否是数字'abc123’.isdigit()
islower()                        # 判断是否是小写
join()                           # 循环取出所有值用xx去连接
lower/upper                      # 大小写转换
swapcase                         # 大写变小写，小写变大写
lstrip/rstrip/strip              # 移除左/右/两侧空白
split()                          # 切割字符串
title()                          # 把每个单词的首字母变成大写
replace(old, new, count=None)    # old被换字符串，new替换字符串，count换多少个。无count表示全部替换
count()                          # 统计出现的次数
index()                          #检测字符串中是否包含子字符串,返回的是下标值.如果没有找到对象的数据,便会报异常

Test='python'
# print(type(Test))
# print('获取第一个字符%s'%Test[0])
# print('获取第二个字符%s'%Test[1])
# for item in Test:
#     print(item,end=' ')
name='peter'
# print('姓名首字母转换大写%s'%name.capitalize()) capitalize 首字母变大写
a='     hello       '
# b=a.strip() #去除字符串中两边的空格
# print(a)
# print(a.lstrip()) #删除左边的空格
# print(a.rstrip()) #删除右边的空格
# 复制字符串
# print('a的内存地址%a'%id(a)) #id函数 可以查看一个对象的内存地址
# b=a #在此只是把a对象的内存地址赋给了b
# print('b的内存地址%d'%id(b))
# print(b)
# dataStr='I love Python'
# print(dataStr.find('M')) #find函数可以查找目标对象在序列对象中的为值,如果没找到就返回-1
# print(dataStr.index('W')) #检测字符串中是否包含子字符串 返回的是下标值
# index如果没有找到对象的数据 便会报异常，而find函数不会，找不到返回-1
# print(dataStr.startswith('I'))  #判断开头
# print(dataStr.endswith('n'))#判断结尾
#
# print(dataStr.lower()) #转换成小写
# print(dataStr.upper())#转换成大写

strMsg='hello world'
# slice [start:end:step] 左闭右开  start<=value<end 范围 顾头不顾腚
# print(strMsg) #输出完整的数据
# print(strMsg[0])
print(strMsg[2:5]) #2-5下标之间的数据
print(strMsg[2:]) #第三个字符到最后
print(strMsg[:3]) #1-3    strMsg[0:3]=strMsg[:3]
print(strMsg[::-1]) #倒叙输出  负号表示方向  从右边往左去遍历
# 共有方法  +  *  in
# 字符串合并
strA='人生苦短'
strB='我用Python'
# list 合并
listA=list(range(10))
listB=list(range(11,20))
print(listA+listB)
# print(strA+strB)
# 复制 *
# print(strA*3)
# print(listA*3)
# in  对象是否存在 结果是一个bool值
print('我' in strA) #False
print(9 in listA)  #False
dictA={"name":"peter"}
print("name" in dictA)
