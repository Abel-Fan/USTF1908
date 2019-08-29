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
# import requests
# from lxml import etree
# url = "http://soso.huitu.com/search?kw=中秋"
#
# res = requests.get(url)
# htmltext = res.text
# html = etree.HTML(htmltext)
# imgurls = html.xpath('//div[@class="seozone"]/a/img/@src')
#
# def download(url):
#     res = requests.get(url)
#     imgData = res.content # 二进制图片数据
#     # 保存文件
#     arr = url.split("/")
#     filename = arr[-1]
#     with open("img/"+filename,"wb") as f:
#         f.write(imgData)
#     print(filename+"-下载完成.")
#
# for file in imgurls:
#     download(file)


# 装饰器
# 目的：
# 1、不改变原函数 2、不改变原函数的调用方式 3、在1、2基础上完成增加新的功能。
# import time
# def fun2(fn):
#     def newFn():
#         start = time.time()
#         fn()
#         end = time.time()
#         print("总时长为：%s"%(end-start))
#     return newFn
# @fun2
# def fn():
#     time.sleep(1)
#     print("hello world")
# fn()
# import time


# def newFn(fn):
#     def newFun():
#         start = time.time()
#         fn()
#         end = time.time()
#         print("总时间%s"%(end-start))
#     return newFun
#
#
# @newFn
# def fn():
#     print("hello word")
#
#
# @newFn
# def fn1():
#     time.sleep(1)
#     print('山西优逸客')




# 装饰器 =  高阶函数 + 闭包 + python固定语法
# 装饰器使用场景

# 装饰器函数
import time,requests
def wrap(fn):
    def newfn(*args,**kwargs):  # args = ("https://www.baidu.com",'xb','男')
        start = time.time()
        fn(*args,**kwargs)   # 解包  fn('https://www.baidu.com','xb','男')
        end = time.time()
        print("总运行时间:%s"%(end-start))
    return newfn

@wrap
def aa(url,name,sex,age=18):
    print(name,sex,age)
    res = requests.get(url)
    print(res.text)

aa("https://www.baidu.com",'xb','男')