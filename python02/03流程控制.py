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

for i in range(10):
    for j in range(10):
        print("*")

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

# while
