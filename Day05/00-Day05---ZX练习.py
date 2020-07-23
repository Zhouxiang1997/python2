def fff(a):
    result = a
    n = 6
    for i in range(1, n + 1):
        result = result * i
    print(result)


fff(1)

print('.............................---.........................................')
myname = '周翔'
name = '庄悦'


def my():
    # name='zx'
    print('{} {}'.format(name, myname))
    pass


def test():
    name = '范冰冰'
    print(myname)
    pass


my()
test()

print('.............................---.........................................')


def change():
    '''
    修改全局变量
    :return:
    '''
    global name
    name = '刘慧敏'
    pass


change()
print(name)
print('.............................---.........................................')
a = 1


def fun(x):
    print(id(x))
    x = 2
    print(id(x))
    pass


print('a的地址{}'.format(id(a)))
fun(a)
print(a)


li = []


def test(parms):
    print(id(parms))
    pass


print(id(li))
test(li)
print('.............................---.........................................')


def cop(x, y):
    '''
    相加
    :param x:
    :param y:
    :return:
    '''
    return x + y


print(cop(2, 4))
def m(x, y): return x + y


print(m(2, 4))
def q(a, b, c): return a * b * c


print(q(1, 2, 3))
age = 30
print('否'if age > 18 else '是')
def funtest(x, y): return x if x > y else y


print(funtest(2, 4))
ea = (lambda x, y: x if x > y else y)(3, 6)
print(ea)


print('.............................---.........................................')


def jiecheng(n):
    result = 1
    for item in range(1, n + 1):
        result *= item
        pass
    return result


print('阶乘{}'.format(jiecheng(3)))


print('.............................---.........................................')


def digui(n):
    '''
    递归函数
    :param n:
    :return:
    '''
    if n == 1:
        return 1
    else:
        return n * digui(n - 1)
    pass


print('阶乘{}'.format(digui(3)))
print('.............................---.........................................')
import os
# def findFile(file_Path):
#     listRs=os.listdir(file_Path)
#     for fileitem in listRs:
#         full_path=os.path.join(file_Path,fileitem)
#         if os.path.isdir(full_path):
#             findFile(full_path)
#         else:
#             print(fileitem)
#             pass
#         pass
#     else:
#         return
#   findFile('F:\\Mari')
import os #引入文件操作模块
def findFile(file_Path):
    listRs=os.listdir(file_Path) #得到该路径下所有文件夹
    for fileItem in listRs:
        full_path=os.path.join(file_Path,fileItem) #获取完整的文件路径
        if os.path.isdir(full_path):#判断是否是文件夹
            findFile(full_path) #如果是一个文件夹 再次去递归
        else:
            print(fileItem)
            pass
        pass
    else:
        return
    pass

# 调用搜索文件夹对象
findFile('E:\\360Downloads')