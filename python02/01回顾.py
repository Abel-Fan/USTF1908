# python
# 语法特点：面向对象的、动态类型、强类型语言。严格的缩进模式

# 注释：
# 单行注释   #
# 多行注释   """ """   ''' '''

# 输入输出
# input(info)  info:用户提示信息
# print([arg1,arg2,....]) 参数不限 参数可以是 变量、值、表达式
# end 输出内容末位的字符，默认\n
# name = "小白"
# print(name,19,20+56)
# print("123",end="")
# print("456",end="")

# 变量
# 变量定义：可变的数据
# 变量的定义语法：
# 简单定义    name="小白"
# 链式定义    name=name1="小白"
# 多元定义    name1,name2,nam3 = 小白,小黑,小红
# 变量名 命名的规范：
#   1.变量名只能由字母、数字、下划线构成 数字不能开头 中文也可以作为变量名
#   2.不能使用关键字和保留字  del list  print input
#   3.严格区分大小写
#   4.尽量语义化

# 数据类型（8个）
# Number( int | float )
# 二进制  八进制 十进制  十六进制
# 科学记数法

# Str
# 字符编码：ASCII GBK GB2312 UTF-8 unicode
# 语法：  ''  ""  ''' '''  """ """
# 转义字符:  \" \' \\  \n \r \t
# 字符前缀： r"" 取消转义字符
#     r"\n"    \n
# 切片工具
# [start:end:step]
# 补充： 模板字符串
# s d f
# 语法
# t1 = '%s/%s/%s %s:%s:%s'%(2019,8,27,9,6,10)
# t2 = '%d/%2d/%2d'%(2019,1,1)
# t3 = '%d/%2d/%2d'%(2019,11,11)
# p1 = "$%0.2f"%(30)
# print(p1)

# None

# Bool
# True False

# List
# 定义: 用来存储一系列相关数据的集合
# 语法： [item1,item2,...]
# 注意：可以创建空列表、含有一个元素的列表；列表元素可以是任意数据类型
# [ [] ,[], True,None ,"sdf",123,{},{'name':'小白'}]
# 二维列表与多维列表
# 基本操作
#  1.addItem
#  2.delItem
#  3.deitItem
#  4.访问 item

# arr1 = [ [1,2] , [3,4] ]
# 访问
# print(arr1[0][0])

# Tuple
# 元组：不可改变的列表
# 语法： t1 = (item1,item2,...)
# 注意： 元组可以创建空元组 ，也可以创建只有一个元素的元组,形式：(1,)。
# t1 = ([1,2],[3,4])
# t1[0][0]="aa"
# print(t1)



# 浅拷贝 与 深拷贝
# arr1 = [1,2,3,4]
# arr2 = arr1

# arr2 = []
# arr2.append(arr1[0])
# arr2.append(arr1[1])
# arr2.append(arr1[2])
# arr2.append(arr1[3])


# arr1 = [[1,2],[2,3]]
# arr2 = []
# arr2.append(arr1[0])
# arr2.append(arr1[1])
#
# arr2[0][0]="aa"
# print(arr1)

import copy

# arr1 = [1,2,3]
# arr2 = copy.copy(arr1)
# arr2[0] = "aa"
# print(arr1)

# arr1 = [[1,2],[2,3]]
# arr2 = copy.deepcopy(arr1)
# arr2[0][0]="aa"
# print(arr1)

# 字典
# 语法：{'键':'值',}   键值对
# 注意： 值可以是任意类型，键必须是不可变数据，字典没有顺序的。
# 基本操作
# 访问
# 添加
# 删除
# 修改

# 集合
# 语法 {item1,item2,...}
# 注意点：集合是不重复的
# 操作
# 添加 update  add
# 删除 remove pop(首位删除)
# 交并补

# 数据类型转换
# int float str bool list set