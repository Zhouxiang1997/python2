# 逻辑运算符  and or not
# and 规则 x and y , x 和y 同为真【True】 结果才为真，否则结果就为假
# 定义四个变量

a,b,c,d=20,13,2,14
# 操作是bool类型的表达式
# print(a+b>c*d and c+d<a) #True
# print(a+b>c*d and c+d>a) #False
# 操作数字和其他类型表达式
# x and y：如果x非零或者True, 运算的结果是：y 如果x为零，则结果为0
# print(a and b)
# print(1 and 20)
# print(12 and 23)
# print(0 and 34)
# print(0 and 12)
# or 逻辑或  x or y ,x 或者y 只要有其中一个条件为真,结果就为True
print('----------------or-----------------------------')
# print(a-b>d or c>a) #全部为False  结果是false
# print(a-b<d or c>a)
# or 操作数字和其他类型表达式
# 如果x非零或者True 则结果为x，如果x为零 则结果为y
# print(a or b) #b
# print(1 or 3) #3
# print(3 or 12) #12
# print(0 or 6) #6
# not 取反 真假切换
# print(not 2>3)
# print(not True)
# 优先级
# ()->not-->and-->or
# 例子
print(2>1 and 1<4 or 2<3 and 9>6 or 2<4 and not 3<2)



