# 本章主要讲述3大相关内容提取器： `re` `BeautifulSoup` `Xpath`
## 01 `re` 正则表达式
### 本节主要介绍了`re` 正则表达式的用法和主要的一些规则，并且进行一些例子的演示。相关详细的文件请查看 py 文件
## 02 糗事百科-正则表达式
### 目标分析：要爬取糗事百科上面的热图的所有的图片。
### 相关操作：
### 1.找到相关的标签，使用正则表达式进行内容的提取。
### 2.创建文件夹：首先进行判断，如果没有这个文件夹才可以进行相关文件夹的创建，如果有的话，不进行文件夹的创建。
        dirname = '糗图'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
### 3.进行主函数的编写：1.生成请求的对象。2.发送请求。3.解析内容，提取相关的图片信息，下载图片。
#### 目标网站：https://www.qiushibaike.com/imgrank/page/1/ 
## 03 雨露文章-正则表达式
### 目标分析：1.进入网站之后提取相关语录的标题。2.然后点击题目之后在提取详细的内容和图片。
### 相关操作：
### 1.拼接 url ，并且请求头部信息`headers`。
        url = url + 'list_' + str(page) + '.html
### 2.构建请求对象,进行解析详细网页的文字和图片。
### 3.正则表达式进行提取相关联的信息。
### 4.遍历整个元组，处理全部的详细页面的`url`和标题。
    for href_title in lt: # 处理全部的详细页面的url和标题
        a_href = 'http://www.vipyl.com/' + href_title[0]
        # print(a_href) 检测拿到的详细页面的url是正确的
        # print(a_href)
        title = href_title[1]
        text = get_text(a_href)
### 5.构建主函数：def main():
        start_page = int(input('请输入你要开始的页码:'))
        end_page = int(input('请输入你要结束的页码:'))
#### 目标网站：http://www.vipyl.com/article/139/list_1.html
## 04 `bs4`详细介绍：`BeautifulSoup`
### 相关介绍：本节主要介绍第二个内容提取器`BeautifulSoup`的使用。主要包括以下的介绍（更详细请查看py文件）。
### 1.根据标签名字查找。
        print(soup.a)
        print(soup.div)
### 2.根据属性值来获取。
        print(soup.a['title'])
        print(str(soup.a.attrs))
### 3.`find`,`find_all`方法。
        print(soup.find('a', title='q')) # 找到第一个 a 标签
        print(soup.find_all('a')) # find_all 找到所有的 a 标签
### 4.`select`根据选择器来选择指定的内容。
        print(soup.select('.tang>ul>li>a')[1].text) # 获取文字
        print(soup.select('.tang>ul>li>a')[1]['href']) # 获取网址
## 05 智联招聘-bs4
## 06 `Xpath`讲解
## 相关介绍：本节主要介绍第三个内容提取器`Xpath`的使用。主要包括以下的介绍（更详细请查看py文件）。
### 1.相关定义：什么是Xpath?
### 2.常用的路径表达式：
        # //：不考虑位置的查找
        # ./:从当前的节点开始向下进行查找
        # @:选取属性
### 3.实例化演示相关例子：以百度为例。
#### 目标网站：https://www.baidu.com/
## 07 `Xpath`练习-好段子
### 项目介绍：抓取好段子网站的标题，内容，进行持久化的存储。
### 相关操作：
#### 1.定义主函数，传入起始页和结束页，循环遍历每一URL进行解析段子文章。
        start_page = int(input('请输入起始页码：'))
        end_page = int(input('请输入结束页码：'))
#### 2.发起请求：构造请求头`headers`。
        request = urllib.request.Request(url=url, headers=headers) # 发起请求
#### 3.读取内容：
        content = urllib.request.urlopen(request).read().decode('utf-8')  # 编码格式为charset=utf-8
#### 4.内容的解析：使用`xpath`即可。
        text = text.replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "") # 去除所有的回车符\r和换行符\n，去除空格，去除\u3000
#### 5.将爬取下来的信息以字典的形式进行存储。
        item_list.append(item) # 将内容添加到字典中去,append添加的意思，将item添加到字典中去
#### 6.数据的可视化存储。
## 08 `xpath`练习—站长网站图片爬取(懒加载问题)
### 项目需求:首先获取网页的全部类型，然后根据用户输入的用户类型进行爬取制定页码的图片
#### 目标网站：https://sc.chinaz.com

