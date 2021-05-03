# Web-Crawler
# 网络爬虫基础到进阶（课程系列学习）
## 目录
### 1.Bs4解析
#### 01.介绍BeautifulSoup（现已内嵌到bs4库下面）的用法，实例爬取的是北京新发地的蔬菜价格，并且进行可持久化存储（csv文件），网页蔬菜的价格主要以表格的形式表现，首先获取表格的源代码，先找到每行，在遍历每一列即可。
#### 02.爬取优美图库的相关联的照片，进行可视化存储。
### 2.Xpath解析
#### 采用 lxml 库下面的 etree 进行提取猪八戒网站，提取相关的价格，目标标题，名字。
### 3.综合训练
#### 目标分析：综合练习爬取网易云音乐的评论
#### 相关介绍：1.网易云音乐的评论在源代码里面看不到，因为是json阿贾克斯请求，必须导入 json包 进行提取 2.通过Chrome浏览器开发者工具的分析，发现评论信息以被加密，必须进行解密 3.最后提取相关评论，进行可视化存储。
### 4.多线程
#### 01.在单线程的状态下，爬取相关的网站数据缓慢，在本节项目下使用多线程 ThreadPoolExecutor 模块进行高效率爬取北京新发地的菜价（对照BS4 01项目），首先对蔬菜价格进行提取，然后创建线程池，将任务传送给线程池，最后将数据写入csv文件，进行可视化存储。
### 5.Selenium 浏览器模拟
### 6.WebSpider基础知识讲解
#### 本章节为WebSpider基础知识讲解和复习，并且对现有知识进行相应的扩充。具体查看文件夹下的 readme.md 文件。
