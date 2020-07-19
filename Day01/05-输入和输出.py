# 输出 %占位符
# me='我的'
# # # classPro='清华附中一年3班'
# # # age=7
# # # print('%s名字是小明: 来自【%s】 今年%d岁了'%(me,classPro,age))
# # # print('%s名字是胖虎: 来自【%s】 今年%d岁了'%(me,classPro,age))
# # # print('%s名字是小叮当: 来自【%s】 今年%d岁了'%(me,classPro,age))
# # # print('我可以\n换行吗') #\n换行效果
# 练习输出
# 姓名: 老夫子
# QQ:66666666
# 手机号:5024193635
# 公司地址:广州市白云区1
#
# name='老夫子'
# QQ='66666666'
# phone='5024193635'
# addr='广州市白云区1'
# print('姓名:{} 年龄是:{} 岁'.format(name,23))
# print('QQ:{}'.format(QQ))
# print('手机号:{}'.format(phone))
# print('地址:{}'.format(addr))
# print('------------以上是format形式的-------------------')
# print("姓名:%s"%name)
# print("QQ:%s"%QQ)
# print("手机号:%s"%phone)
# print("地址:%s"%addr)
#格式输出的其他方式 .format()

# input的练习  获取键盘输入的内容
name=input("请输入您的姓名:")
age=int(input("请输入您的年龄:"))
print(type(name))
QQ=input('请输入您的qq')
phone=input("请输入您的电话:")
addr=input("请输入您的地址:")

print('姓名:%s 年龄是:%d 岁'%(name,age))
# print('姓名:{} 年龄是:{} 岁'.format(name,age))
print('QQ:{}'.format(QQ))
print('手机号:{}'.format(phone))
print('地址:{}'.format(addr))