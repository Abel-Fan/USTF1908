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
import requests
from lxml import etree
url = "http://soso.huitu.com/search?kw=中秋"

res = requests.get(url)
htmltext = res.text
html = etree.HTML(htmltext)
imgurls = html.xpath('//div[@class="seozone"]/a/img/@src')

def download(url):
    res = requests.get(url)
    imgData = res.content # 二进制图片数据
    # 保存文件
    arr = url.split("/")
    filename = arr[-1]
    with open("img/"+filename,"wb") as f:
        f.write(imgData)
    print(filename+"-下载完成.")

for file in imgurls:
    download(file)