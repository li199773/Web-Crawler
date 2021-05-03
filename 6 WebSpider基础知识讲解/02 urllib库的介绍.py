"""
urllib 库
模拟浏览器请求的库，Python自带的库
有两个版本：
python2: urllib urllib2
python3: urllib.request urllib.parse
现在大部分还是使用python3居多，但是网上一些博客写的还是python2的一些内容，

response相关的知识点：
    read() 读取相应的内容，内容是字节类型
    geturl() 根据传入的目标网址来获取相应的url
    getheaders() 获取头部信息，列表里面有元组
    getcode() 获取状态码
    readlines() 按行读取，返回列表，都是字节类型（一般情况下不使用）
"""
# import urllib.request
#
# url = 'http://www.baidu.com'
# # 在写代码的时候必须要写完整的url
# resposen = urllib.request.urlopen(url=url)
# url.request.urlopen() 使用urllib来打开目标的网址

# print(resposen.geturl())
# print(dict(resposen.getheaders()))
# print(resposen.getcode())
# print(resposen.readlines())

# print(resp.read().decode())
# 也可以进行写入文件中进行查看
# 有2种写入的方式
# 1.with open('baidu.html', 'w', encoding='utf-8') as fp:
#     fp.write(resposen.read().decode())
# 2.
#with open('baidu1.html','wb') as fp:
#    fp.write(resposen.read()) # wb就以字节类型进行存储，不用再写encoding='utf-8'

# 2 下载图片
import urllib.request

img_url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fattach.bbs.miui.com%2Fforum%2F201110%2F28%2F084714m51zkooi5omrcinx.jpg&refer=http%3A%2F%2Fattach.bbs.miui.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1622271713&t=93de2cd723daffe659459133166245a0'
resposen = urllib.request.urlopen(img_url)
# 像图片只能写入二进制的格式
"""
urllib.request.urlopen(url)
"""
# 1.with open('meinv.jpg','wb') as fp:
#     fp.write(resposen.read())
"""
urllib.request.urlretrieve(url,image_path/image_name（目标的路径或者目标的名字）)
"""
# 2.第二种方案,进行直接性质的写入，不需要返回
urllib.request.urlretrieve(img_url,'美女.jpg')


