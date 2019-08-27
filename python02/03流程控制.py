# 流程控制
# 1、分支语句
# if
# 语法
"""
#单路分支
if a>2:
    print(a)

# 双路分支
if a>b:
    print("a>b")
else:
    print("b>a")

# 多路分支
if cj>90:
    print("优秀")
elif cj>85:
    print("良好")
elif cj > 60:
    print("及格")
else:
    print("不及格")
"""
# 登录功能
# username
# password



# 2、循环语句
# for
# 语法
"""
for 变量 in 可迭代对象:
    循环体
    
for(var i=0;i<10;i++){
    
}
"""

# for item in "abcdef":
#     print(item)

# 遍历：依次访问列表中的元素
# for item in [1,2,3,4,5,6]:
#     print(item)
# for item in (1,2,3,4,5,6):
#     print(item)

# range(start,end,step)  #

# for i in range(10):
#     print(i)


# 嵌套for循环
#
# for i in range(10):
#     for j in range(10):
#         print("*")

"""
*****
*****
*****
*****

*
**
***
****
*****
九九乘法表
"""
# for i in range(10):  #  行
#     for j in range(10): # 列
#         print("*",end="")
#     print("")

# for i in range(10):
#     print("*"*10)


# for i in range(1,11):
#     for j in range(i):
#         print("*",end="")
#     print("")
# for i in range(1,11):
#     print("*"*i)



# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%dx%d=%2d "%(j,i,j*i),end="")
#     print("")

# 数组推导式
# arr1 = [1,2,3,4,5,6]
# arr2 = [ item**2 for item in arr1]
# arr3 = [ item**2 for item in arr1 if item%2==0]
# print(arr3)

# list 转化为 str
# ",".join(['1','2','3','4'])
"""
1x1=1\n1*2=2 2*2=4\n
"""
# print(    "\n".join([ " ".join([ '%d*%d=%2d'%(j,i,j*i) for j in range(1,i+1) ]) for i in range(1,10)] )   )
# 干预循环
# break 跳出循环

# for i in range(10):
#     if i%2==0:
#         print("偶数%s"%i)
#         break
# else:
#     print("end")



# while
# 语法
# while 条件:
#     循环体
# 猜数字

# import random
# num = random.randint(0,100)
#
# while True:
#     num1 = int(input("请输入一个数（0-100）:"))
#     if num1>num:
#         print("您输入的数字过大")
#     elif num1<num:
#         print("您输入的数字过小")
#     else:
#         print("恭喜您答对了！！")
#         break

# while for区别
# for明确迭代对象或明确循环次数
# while 明确循环条件

# 干预循环 break 退出循环   continue 退出本次循环，直接开始下次循环

for i in range(5):
    if i==2:
        # continue
        break

    print(i)