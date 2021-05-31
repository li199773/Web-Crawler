"""
简单使用：
    说明:选择器
    导入方式：from bs4 import beautifulSoup
    使用方式：可以将html文档转换成指定的对象，然后通过对象的方法或者属性去查找指定的内容
    2种方法：
    (1)转化本地文件：
        soup = BeautifulSoup(open('本地文件'),'lxml')
    (2)转化网络文件:
        soup = BeautifulSoup('字符串类型或者字节类型','lxml')
    lxml是解析器，将相关的文件转换成 soup 的文件,然后可以使用下面的相关的指令
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('BeautifulSoup_text.html', encoding='utf-8'), 'lxml')
# print(type(soup))
# 经过测试之后发现，打印出来的全部是对象，只需要知道相关的方法即可。
# 1.根据标签名字查找
# print(soup.a)
# <a href="http://www.song.com/">宋朝是最强大的王朝，不是军队的强大，是经济的强大</a>
# print(soup.div)
"""
通过标签名字查找只能找到第一个符合相关的标签
"""
# 2.根据属性值来获取
# 无非就是想获取a href 里面的网址和标签下的文字信息即可
print(soup.a['href'])
print(soup.a['title'])
# 缺点是还是会打印出来第一个
print(soup.a.attrs['href'])
print(soup.a.attrs)  # 此时返回的是一个字典
print(str(soup.a.attrs))  # 此时返回的是一个字典
# attrs 可以传回来所有的元素值=print(soup.a.attrs['href'])
# 获取内容
soup.a.string
# 这个登记比较低,如果标签里面还有标签的话，那么输出的为空 None
soup.a.get_text()
print(soup.a.text)
# 这两个可以获取文本，等级比较高
print(soup.div.text)
print(soup.div.string)
print(soup.div.get_text())
# 3.find方法
print(soup.find('a', title='q'))
# 找到第一个 a 标签
print(soup.find_all('a'))
# find_all 找到所有的 a 标签
print(soup.find('a', alt='q'))
print(soup.find('a', class_='q'))
# class是关键字，要想取用class的话必须要用class_来去写
print(soup.find_all('a'))
print(soup.find_all('a', limit=2))
# limit = 2是在全部的里面取前两个
# 4.select
# 根据选择器来选择指定的内容
"""
常见的选择器：
(1)标签选择器：a
(2)类选择: .dd
(3)id选择器: #dd
(4)组合选择器: .dd,#dd,nne
(5)层级选择器:
(6)伪类选择器:
(7)属性选择器:
"""
print(soup.select('.tang>ul>li>a')[1])
print(soup.find_all('a')[-1])
# 只要是选择器，返回的就是列表
print(soup.select('.tang>ul>li>a')[1].text)
# 获取文字
print(soup.select('.tang>ul>li>a')[1]['href'])
# 获取网址
print(str(soup.a.attrs).split(','))
print(str(soup.a.attrs))
