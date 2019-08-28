# 流程控制
# 分支语句 循环语句

"""
if num>90:
    pass
elif num>80:
    pass
else:
    pass
"""

"""
# for循环 明确循环次数,明确迭代对象.
range(start,end,step)
# while 明确循环条件,不明确循环次数

# pass 占位
# else 只有在循环结束并且没有break时触发
# 干预循环 break continue

列表的遍历
列表的推导式 一行代码完成九九乘法表
元组

字典遍历
"""
obj = {'name':'小白','age':'18','sex':'男'}
# for item in obj:
#     print(item)
#     print(obj[item])

# for item in obj.keys():
#     print(item,obj[item])

# for item in obj.values():
#     print(item)

# for k,v in obj.items():
#     print(k,v)

# 字典推导式
# print({ v:k for k,v in obj.items()})
# print({ k:"xm" for k in obj if k=="name"})
#         'a':[1,2,6,7] 'b':[3,4,8,9]
# obj = {'a':[1,2],"B":[3,4],"A":[6,7],"b":[8,9]}
#
# obj2 = { k.upper():obj.get(k.upper())+obj.get(k.lower()) for k,v in obj.items() if k in ['a','b']}
# print(obj2)

# 集合推导式
# s1 = {1,2,3,4,5,6}
# s2 = { i**2 for i in s1 if i%2==0}
# print(s2)
