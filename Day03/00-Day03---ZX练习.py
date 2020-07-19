# test='python'
# print(type(test))
# print('获取第一个字符%s'%test[0])
# print('获取第一个字符%s'%test[4])
# for item in test:
#     print(item,end=' ')name
# name='peter'
# print('%s'%name.capitalize())
# print(format(name).capitalize())
# a='      hello      '
# a.strip()
# print(a.strip())
# a.lstrip()
# print(a.lstrip())
# print(a.rstrip())
# b=a
# print(b)
# print(format(id(a)))
# print(format(id(b)))
# data='i love python'
# print(data.index('i'))
# print(data.startswith('i'))
# print(data.endswith('n'))
# print(data.lower())
# print(data.upper())
# print(data.capitalize())
# print(data[2:5])
# print(data[2:])
# print(data[:3])
# print(data[::-1])
# li=[]
# li=[1,2,3,'你好']
# print(type(li))
# print(len(li))
# listA=['abcd',785,12.23,'qiuzhi',True,785]
# print(listA[1:3])
# print(listA[2:])
# print(listA[::-1])
# print(listA*2)
# listA.append(['dsds',22])
# print(listA)
# listA.append(123)
# print(listA)
# listA.insert(1,'zhoux')
# print(listA)
# a=list(range(10))
# print(a)
# listA.extend(a)
# print(listA)
# listA=['abcd',785,12.23,'qiuzhi',True,785]
# print('修改之前',listA)
# listA[2]=111
# print('修改之后',listA)
# listB=list(range(10,50))
# print(listB)
# del listB[0:2]
# print(listB)
# listB.pop(1)
# print(listB)
# listB.pop(3)
# print(listB.index(42,40,45))
# q=('23e213e',34,45.444,[11,23,4434])
# print(type(q))
# print(q)
# # for item in q:
# #     print(item,end=' ')
# #     pass
# # print(q[2:4])
# print(q[::-1])
# print(q[::-2])
# w=()
# print(w)
# q=('23e213e',34,45.444,[11,23,4434])
# print(type(q[3]))
# print(q)
# q[3][0]=1
# print(q)
# tupleq=('1',)
# print(tupleq)
# print(type(tupleq))
# tuplew=tuple(range(10**2))
# print(tuplew)
dictA = {'pro': '艺术', 'school': '北京电影学院'}
dictA.update({'ddd': '20'})
print(dictA)
dictA['name'] = '李易峰'
dictA['age'] = '30'
dictA['pos'] = '歌手'
# print(type(dictA))
# print(dictA)
# print(len(dictA))
# print(dictA['name'])
# dictA['name']='谢霆锋'
# print(dictA)
# print(dictA.keys())
# print(dictA.values())
# print(dictA.items())
# for item in dictA.items():
#     print(item)
#     print('%s=%s'%(key,value))
print(sorted(dictA.items(), key=lambda a: a[0]))
print(sorted(dictA.items(), key=lambda d: d[1]))

listA = list(range(10))
listB = list(range(10, 20))
print(listA + listB)
listA = listA * 4
print(listA)
print(listA.count(3))
print(22 in listA)
print(2 in listA)
steA = '入手苦短'
steB = '我用爬虫'
print(steA * 3)
print(steA + steB)
print('用' in steA)
print('入' in steA)
dictB = {'mane': 'zx'}
print('name' in dictB)
print('mane' in dictB)
