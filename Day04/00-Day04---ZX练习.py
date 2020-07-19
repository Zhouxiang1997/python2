# print('校长的升高是%f' % 1.73)
# print('校长的体重是%f' % 160)
# print('校长的爱好是%s' % '唱歌')
# print('..................or...................')
# print('校长的升高是%f' % 1.73)
# print('校长的体重是%f' % 160)
# print('校长的爱好是%s' % '唱歌')
# def printinfo(name, height, weight, hobbies, pro):
#     '''
#     这个函数是用来打印校长信息的组合
#     :return:
#     '''
#     print('%s的升高是%f' % (name, height))
#     print('%s的体重是%f' % (name, weight))
#     print('%s的爱好是%s' % (name, hobbies))
#     print('%s的专业是%s' % (name, pro))
#     pass
#
#
# printinfo('小哥', 189, 70, '打游戏', '犯罪')
# print('..................or...................')
# printinfo('小香', 149, 50, '看电视', '抢劫')
# # printinfo()   #ctrl 放上去就可以看出函数介绍
# # printinfo()
# # printinfo()
# # printinfo()
# # print('wdnmd')
# def sum(a,b):
#     sum=a+b
#     print(sum)
#     pass
# sum(2,42)
# sum(22222,445456)
# def sum1(a,b=30):
#     print('默认=%d'%(a+b))
#     pass
# sum1(2)
# sum1(22,33)
# sum1(10)
# def getcomputer(*args):
#     '''
#     计算累加和
#     :param args:
#     :return:
#     '''
#     result=0
#     for item in args:
#         result+=item
#     print('result=%d'%result)
#     pass
# getcomputer(1,3,4,5,5,2,5)
# getcomputer(1)
# getcomputer(2,4,5)
#
# def keyFunc(**kwargs):
#     print(kwargs)
# # keyFunc(1,3,4)
# dictA={'name':'zx','age':23}
# keyFunc(**dictA)
# keyFunc(name='cx',age=21)
# keyFunc()
# def complexFunc(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     pass
# complexFunc(1,3,4,name='zx')
# complexFunc(gae=33)
# def sum1(a,b=30):
#     print('默认=%d'%(a+b))
#     pass
# sum1(1)
# def sum(a,b):
#     sum=a+b
#     return sum
#     pass
# def calcomputer(num):
#     lis=[]
#     result=0
#     i=1
#     while i<=num:
#         result+=i
#         i+=1
#         pass
#     lis.append(result)
#     return lis
#
# va=calcomputer(10)
# print(va)
# print(type(va))
def returnTuple():
    '''
    返回元组类型
    :return:
    '''
    # return 1,2,3
    return {'name': "dd"}


print(type(returnTuple()))
print('................................')


def function1():
    print('1234567')
    print('33344')
    print('vvxs2')
    pass


def function2():
    print('调用func2')
    function1()
    print('fssssssssss')
    pass


function1()
print('................................')
function2()
