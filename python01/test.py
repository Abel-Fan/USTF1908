# <!-- -->
# //  /**/
# 单行注释
"""
多行注释
"""
'''
多行注释
'''

# 输入输出工具
# input(提示信息)
#
# js var aa = "asdf"
# name = input("请输入你的名字：")

# 输出工具
# print()
# 可以跟多个参数,可以传递 变量 数据 表达式
# print(name)
# print("周润发","周润发",123,123+456)

# 变量： 可改变的数据
# 语法
# 变量名命名规则
# 你好="hello"
# print(你好)
"""
1.  变量名由 字母 数字 下划线 组成 数字不能开头 ，也可以使用中文
正确：name1 name2 
错： 1name 2name 
2、 不能使用关键字和保留字
3、 严格区分大小写
4、 尽量语义化

"""
"""
变量名 = 值
# 链式赋值
变量名1=变量名2=10
# 多元赋值
变量1,变量2,变量3,变量4=1,2,3,4

js
变量1=值1,变量2=值2,变量3=值3
"""
# num1 =10
# num2=num3=20
# print(num1,num2,num3)
# num1,num2,num3=10,20,30
# print(num1,num2,num3)

# 数据类型
# 数字类型
# num = 2 #
# num1 = 10 #  8 4 2 1
# 整型 浮点型
# 00000000
# 10 20 0 -20   1.2 1.3 1.0
# 科学计数法
# 1e4
# 二进制0b 八进制0o 十进制 十六进制0x
# 10 1010


# 字符串类型
# 字符编码
# ASCII GBK GB2312 UTF-8 unicode
# 定义字符串
# js '' ""  ``
# python ''  ""  """"""  ''' '''
# str1 = "山西" \
#        "优逸客"
# str2 = '陕西优逸客'
# str3 = """优斯特"""
# str4 = '''山西硬汉'''
#
# str5 = " I'm "
# str5 = """
# asdf
# aasdf
# asdf
# asd
# f
# """
# 转义字符
str1 = " \" \"\" "
str2 = '\''
str3 = "\\abc"
"""
\\
\'
\"
\n 换行
\r 回车
\t 制表符
"""
# 字符前缀
# r取消转义作用
str1 = "山西优逸客"
       # 0 1 2 3 4
       #  ... -2-1
# 从字符串中获取字符
# str1[index]   str1[0]
# print(str1[4])
# print(str1[-1])
# 切片
# 变量名[start:end,step]
# str1 = "hello world"
# print(str1[-6::])

# None
# 布尔值 True False

# list列表 数组
# 用来存储一系列相关数据的集合
# 语法
# arr1 = []
# arr2 = [1]
# 一维列表
arr1 = [56,76,78,47,90]
# 二维列表
# arr2 = [[1,2],[3,4],[5,6]]
# 多维列表
#arr3 = [[1,2],[2,3],[[3,4],[6,7]]]

#基本操作
arr = [1,2,3,4,5,6,7,8,9]
# 1、访问元素
# arr[index]
# print(arr[0],arr[-1])
# print(arr[0:5])  # 截取
# 2、添加元素
# arr.append('aa')  # 末尾添加
# print(arr)
# arr.insert(5,"aa")
# print(arr)
# 3、修改元素
# arr[0] = "aa"
# print(arr)
# 4、删除元素
# arr.remove(1) # 删除值为1的元素
# print(arr)
# arr.pop(2)  # 删除下标为2的元素
# print(arr)
# del arr[5]
# print(arr)
# 5、遍历元素

