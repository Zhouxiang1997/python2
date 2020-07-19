# score=70
# if score<=60:
#     print('成绩不合格')
#     pass
# elif:
#     print('成绩合格')
#     pass
# print('结束')
# score=int(input('你的成绩'))
# print(type(score))
# if score>=90:
#     print('成绩优秀')
#     pass
# elif score>=60<90:
#     print('成绩良好')
#     pass
# elif score<60:
#     print('成绩不合格')
#     pass
# print('结束')
# 0：石头 1：剪刀 2：布
# input(random)
# 计算机 人
# import random
# person=int(input('出拳：【0：石头 1：剪刀 2：布】'))
# computer=random.randint(0,2)
# if person==0 and computer==1:
#     print('你赢了')
#     pass
# elif person==1 and computer==2:
#     print('你赢了')
#     pass
# elif person==2 and computer==0:
#     print('你赢了')
#     pass
# elif person==computer:
#     print('平手')
#     pass
# else:
#     print('你输了')
# xuefen=int(input('请输入您的学分'))
# if xuefen>10:
#     chengji=int(input('请输入您的成绩'))
#     if chengji>80:
#         print('升学')
#         pass
#     else:
#         print('您的成绩达不到升学标准')
#         pass
#     pass
# else:
#     print('学分达不到')
#
# index=1
# while index<=100:
#     print(index)
# import random #直接导入产生随机数的模块
# # 计算机  人
# count=1
# while count<=10:
#     person=int(input('请出拳:[0:石头 1:剪刀 2:布]'))
#     computer=random.randint(0,2)
#     if person==0 and computer==1: #多条件
#         print("厉害了..你赢了")
#         pass
#     elif person==1 and computer==2:
#         print("厉害了..你赢了")
#     elif person==2 and computer==0:
#         print("厉害了..你赢了")
#         pass
#     elif person==computer:
#         print('不错 居然是平手')
#         pass
#     else:
#         print('哈哈...你输了吧')
#         pass
#     count+=1
# row=9
# while row>=1:
#     col=1
#     while col<=row:
#         print('%d*%d=%d'%(row,col,row*col),end=' ')
#         col+=1
#         pass
#     print()
#     row-=1
# rool=1
# while rool<=7:
#     j=1
#     while j<=rool:
#         print('*',end=' ')
#         j+=1
#     print()
#     rool+=1
# rool=7
# while rool>=1:
#     j=1
#     while j<=rool:
#         print('*',end=' ')
#         j+=1
#     print()
#     rool-=1
# tage='wsddacc'
# for item in tage:
#     print(item)
# sun=0
# for data in range(1,101):
#     sun+=data
#     pass
# print('sun=%d'%sun)
# print('...............for...............')
# for data in range(50,201):
#     if data%2==0:
#         print('%d是偶数'%data)
#         pass
#     else:
#         print('%d是奇数'%data)
# sum=0
# for item in range(1,100):
#     if item%2==0:
#         continue
#         pass
#     print(item)
# for item in 'zhouxiangrool':
#     if item=='o':
#         continue
#         pass
#     print(item)
# idex=1
# while idex<=100:
#     if idex>20:
#         break
#         pass
#     idex+=1
# #     print(idex)
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(i,j,i*j),end=' ')
#         pass
#     print()
# #     pass
# for item in range(1,11):
#     print(item,end=' ')
#     if item>=5:
#         break
#     pass
# else:
# #     print('完成')
# account='zhou'
# pwd='123'
# for i in range(3):
#      zh=input('输入账号')
#      pd=input('输入密码')
#      if account==zh and pwd==pd:
#          print('成功登录')
#          break
#          pass
#      pass
# else:
#      print('账号锁定')
# index=1
# while index<=10:
#     print(index)
#     if index==6:
#         break
#     index+=1
#     pass
# else:
#     print('执行了吗')
# heiht=175
# ege=80.5
# index=(%dege%heiht
# time=0
# while time<=3:
#     age=int(input('请输入您的年龄'))
#     if age==23:
#         print('你猜对了')
#         break
#         pass
#     elif age>23:
#         print('你猜大了')
#         pass
#     else:
#         print('你猜小了')
#         pass
#     time+=1
#     if time==3:
#         choose=input('是否继续玩下去，输入yorn')
#         if choose=='y' or choose=='Y':
#             time=0
#             pass
#         elif choose=='n' or choose=='N':
#             time==4
#             exit('退出')
#             pass
#         else:
#             print('输入yorn')
height=1.75
age=80.5
bmi=age/(height**2)
print('输出bmi的数据%f'%bmi)
if bmi<18.5:
    print('体重过轻')
    pass
elif 18.5<=bmi<25:
    print('体重正常')
    pass
elif 25<=bmi<28:
    print('体重过重')
    pass
elif 28<=bmi<32:
    print('体重肥胖')
    passe
else:
    print('严重肥胖')


