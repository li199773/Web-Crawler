# 本章节主要讲述3大相关内容提取器： `re` `BeautifulSoup` `Xpath`
## 01 `re` 正则表达式
### 本节主要介绍了`re` 正则表达式的用法和主要的一些规则，并且进行一些例子的演示。相关详细的文件请查看 py 文件。
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
