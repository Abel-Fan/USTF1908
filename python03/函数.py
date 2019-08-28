# 函数：封装特定功能的代码块，以便重复调用。

# mysum() 求和函数,作用求任意两个数的和
# 函数语法
"""创建语法
def 函数名([arg1,arg2...]):
    函数体
    [return [value] ]
"""
# def mysum(num1,num2):   #形参：形式参数
#     return num1+num2
"""调用语法
函数名(56,46)
"""
# num = mysum(56,46)
# print(num)

"""
作业
求最大数
myMax()
求最小数
myMin()
求最大数或最小数
myFind()
"""
# def myFind(arr,type):
#     # type min max
#     if type=='max':
#         max = arr[0]
#         for i in arr:
#             if i>max:
#                 max=i
#         return max
#     elif type=='min':
#         min = arr[0]
#         for i in arr:
#             if i<min:
#                 min=i
#         return min
#
# res = myFind([1,2,3,4,5,6,7,8],'min')
# print(res)

# 注意：
"""
1.参数要一一对应,顺序以及数量要保持一致
2.形参只会生成一次
3.返回值可有可无,返回值后不能跟任何内容
4.返回值只能有一个,返回多个值会打包为元组形式
5.return可以有多个,但是只有一个return被运行
"""
# def fn():
#     return 1,2,3,4
# res = fn()
# print(type(res))
#
# a,b,c,d = 1,2,3,4

# 参数用法
# 1、必选参数
# 2、缺省参数（默认参数）
# def myFind(arr,type='max'):
#     # type min max
#     if type=='max':
#         max = arr[0]
#         for i in arr:
#             if i>max:
#                 max=i
#         return max
#     elif type=='min':
#         min = arr[0]
#         for i in arr:
#             if i<min:
#                 min=i
#         return min

# res = myFind([1,2,3,4])
# print(res)
# def append(item,arr=[]):
#     arr.append(item)
#     print(arr)
#
# append(1,[])
# append(2,[])
# append(3,[])


# 可变参数
# def mysum(*arr):
#     num = 0
#     for item in arr:
#         num+=item
#     return num
# res = mysum(1,2,3,4,5,6,7,8)
# print(res)

# 关键字参数
# def fn(**info):
#     print(info)
#
# fn(math=100,en=89,py=80)

# 参数定义的顺序  必选参数-> 默认参数 -> 可变参数 -> 关键字参数
# def fn(type='max',arr):
#     pass
# fn([1,2,3])

# 万能参数
# def fn(*args,**kwargs):
#     print("args:",args)
#     print("kwargs:", kwargs)
# fn([1,2],12,456,"abc",name="xb",cj=45)

# 名词解释
# 高阶函数：返回值或者是参数是另外一个函数的函数
# def fn1():
#     def fn2():
#         print("this is fn2")
#     return fn2
#
# fn2 = fn1()
# fn2()
# fn2()

# def fn(num1,num2,fun):
#     fun(num1,num2)
#
#
# def add(n1,n2):
#     print(n1+n2)
#
# fn(10,20,add)

# 柯里化
# def mysum(num1):
#     def newMysum(num2):
#         print(num2+num1)
#     return newMysum
# mysum(10)(30)

# 闭包：发生嵌套关系的两个函数，内部函数使用外部函数的变量，在全局情况下调用内部函数时形成闭包，用来保护数据
# def fn1():
#     arr1 = []
#     def fn2(item):
#         arr1.append(item)
#         print(arr1)
#     return fn2
# fn2 = fn1()
# fn2(1)
# fn2(2)
# fn2(3)

# 递归：自己调用自己
# 阶乘、深拷贝、拷贝目录
# def jc(num):
#     return (1 if  num==1  else  num*jc(num-1))
#     # if num==1:
#     #     return 1
#     # else:
#     #     return num*jc(num-1)
#
# print(jc(9))

# 作用域：变量起作用的范围。
# 作用域链：

# name = "abc"
# global
# def fn():
#     global name
#     name = "bcd"
#     print(name)  # bcd
#
# fn()
# print(name) #



# nolocal
# name = "abc"
# def fn():
#     name = "bcd"
#     def newFun():
#         nonlocal name
#         name = "def"
#     newFun()
#     print(name) #"def"
# fn()
# print(name) #"abc"

