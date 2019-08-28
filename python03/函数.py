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
def myFind(arr,type):
    # type min max
    if type=='max':
        max = arr[0]
        for i in arr:
            if i>max:
                max=i
        return max
    elif type=='min':
        min = arr[0]
        for i in arr:
            if i<min:
                min=i
        return min

res = myFind([1,2,3,4,5,6,7,8],'min')
print(res)