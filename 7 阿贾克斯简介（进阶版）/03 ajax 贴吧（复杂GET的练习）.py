"""
项目的需求：
输入输入吧名，输入起始页码，输入结束页码，然后在当前文件夹下面创建一个以吧名字的文件夹，里面是每一页的html内容,文件名字是以吧_page.html
"""
import urllib.request
import urllib.parse
# 写入文件的模块
import os


# 目标url：https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150。
# 观察发现：kw=为你要搜索的吧名字，pn=为显示的数目，可以通过（页数-1）*50来获取pn，进行拼接即可。
url = 'https://tieba.baidu.com/f?ie=utf-8'

ba_name = input('请输入你要查找的吧名：')
start_page = int(input('请输入开始的页数：'))
end_page = int(input('请输入结束的页数：')) # 数字 字符串类型，加上int()

if not os.path.exists(ba_name):

# 创建文件夹：
    os.mkdir(ba_name)

# 因为不是查找的一个网页，需要一个循环，来查找每一页的数据
for page in range(start_page,end_page + 1):
    # 在给定的页面的区间里面进行循环，取相关的数字页码
    # page就是当前页面的意思
    data = {
        'kw': ba_name,
        'pn': (page - 1)*50,
    }
    # 拼接url
    data = urllib.parse.urlencode(data)
    url_t =url + data
    # 试验相关的网页地址
    # print(url_t)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',

    }

    # 发送请求
    request = urllib.request.Request(url=url_t,headers=headers)
    print('第%s页开始下载。。。。。' % page) # 提示第几页开始下载
    # 返回
    response = urllib.request.urlopen(request)

    # 生成文件名
    filename = ba_name + '_' + str(page) + '.html'
    # 拼接文件路径
    filepath = ba_name + '/' + filename

    # 写入内容
    with open(filepath, 'wb') as fp:
        fp.write(response.read())
    print('第%s页结束下载。。。。。' % page)  # 提示第几页结束下载



