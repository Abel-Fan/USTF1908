# 函数：封装特定功能的代码块，以便重复调用。

# mysum() 求和函数,作用求任意两个数的和
# 函数语法
"""创建语法
def 函数名([arg1,arg2...]):
    函数体
    [return [value] ]
"""
def mysum(num1,num2):   #形参：形式参数
    return num1+num2
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

