# 匿名函数
# 语法
# lambda [参数1,参数2...] : 函数体
# 举例
"""
def mysum(a,b):
    return a+b

lambda a,b:a+b
"""
# 匿名函数调用语法
"""
mysum = lambda a,b:a+b
mysum(10,20)

自调用
(lambda a,b:a+b)(10,20)
"""
# 辅助高阶函数
# def fn(a):
#     return a**2
# res = map(fn,[1,2,3,4,5])
# res = map(lambda a:a**2,[1,2,3,4,5])
# print(list(res))

# mymap
# def mymap(fn,arr):
#     newarr = []
#     for item in arr:
#         newarr.append(fn(item))
#     return newarr
#
# res = mymap(lambda x:x**2,[1,2,3,4,5,6])
# print(res)
