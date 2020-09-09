print(abs(-12293))
print(round(-12293.345, 1))
print(3**3)
print(pow(3, 3))
print(max([21,44,576,84,76,1212]))
print(sum(range(50),3))
a,b,c=1,2,3
qw=eval('a+b+c')
print('动态执行函数{}'.format(qw))
print('动态执行函数{}'.format(eval('a+b+c*a-30')))
def TestFun():
    print('我执行了吗')
    pass
eval('TestFun()')
print(bin(10))
print(hex(23))
tup=(1,2,3,4)
print(type(tup))
li=list(tup)
print(type(li))
li.append('aiqgznk')
print(li)
tyi=tuple(li)
print(type(tyi))
dic=dict()
print(type(dic))
dic['name']='周翔'
dic['age']=18
print(dic)
print(bytes('我喜欢python',encoding='utf-8'))


#通过构造函数创建空 bytes
b1 = bytes()
#通过空字符串创建空 bytes
b2 = b''
#通过b前缀将字符串转换成 bytes
b3 = b'http://c.biancheng.net/python/'
print("b3: ", b3)
print(b3[3])
print(b3[7:22])
#为 bytes() 方法指定字符集
b4 = bytes('C语言中文网8岁了', encoding='UTF-8')
print("b4: ", b4)
#通过 encode() 方法将字符串转换成 bytes
b5 = "C语言中文网8岁了".encode('UTF-8')
print("b5: ", b5)
#通过 decode() 方法将 bytes 转换成字符串
str1 = b5.decode('UTF-8')
print("str1: ", str1)

print('........................................................................................................')
print(all({}))
print(all([]))
print(all(()))
print(all((1.3,33,'ccc')))
print(all([1,3,0]))
print(all([1,2,4,False]))
print(all([()]))
print('.............................................................................................................')
li = [1,2,3,0]
s=any(li)
print(s)
print(any([0,'',False]))

