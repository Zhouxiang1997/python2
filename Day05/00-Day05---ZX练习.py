def fff(a):
    result = a
    n = 6
    for i in range(1, n + 1):
        result = result * i
    print(result)
fff(1)

print('.............................---.........................................')
myname='周翔'
name='庄悦'
def my():
    # name='zx'
    print('{} {}'.format(name,myname))
    pass
def test():
    name='范冰冰'
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
    name='刘慧敏'
    pass
change()
print(name)
print('.............................---.........................................')
a=1
def fun(x):
    print(id(x))
    x=2
    print(id(x))
    pass
print('a的地址{}'.format(id(a)))
fun(a)
print(a)
