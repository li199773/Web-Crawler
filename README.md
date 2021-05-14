# Web-Crawler
# 网络爬虫基础到进阶（课程系列学习）
# 目录
## 1.Bs4解析
### 01.介绍BeautifulSoup（现已内嵌到bs4库下面）的用法，实例爬取的是北京新发地的蔬菜价格，并且进行可持久化存储（csv文件），网页蔬菜的价格主要以表格的形式表现，首先获取表格的源代码，先找到每行，在遍历每一列即可。
### 目标网址：http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml
### 02.爬取优美图库的相关联的照片，进行可视化存储。
### 目标网址：https://www.umei.cc/bizhitupian/weimeibizhi/
## 2.Xpath解析
### 采用 lxml 库下面的 etree 进行提取猪八戒网站，提取相关的价格，目标标题，名字。
### 目标网址：https://jinzhou.zbj.com/search/f/?type=new&kw=saas
## 3.综合训练
### 目标分析：综合练习爬取网易云音乐的评论。
### 相关介绍：
### 1.网易云音乐的评论在源代码里面看不到，因为是 json 阿贾克斯请求，必须导入 json 包进行提取。
### 2.通过 Chrome 浏览器开发者工具的分析，发现评论信息以被加密，必须进行解密（需要导入 from Crypto.Cipher import AES 包进行解析）。
### 3.最后提取相关评论，进行可视化存储。
### 目标网址：https://music.163.com （任意网易云音乐的评论即可）
## 4.多线程
### 01.在单线程的状态下，爬取相关的网站数据缓慢，在本节项目下使用多线程 ThreadPoolExecutor 模块进行高效率爬取北京新发地的菜价（对照BS4 01项目），首先对蔬菜价格进行提取，然后创建线程池，将任务传送给线程池，最后将数据写入csv文件，进行可视化存储。
### 目标网址：http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml （页码1换成 i 进行遍历，可以获取多个网页）。
### 02.协程练习：协程是当任务阻塞的情况下，会自动的切换成未阻塞的任务上。在宏观上是多任务一起在执行，在微观上是看是一个任务一个任务在切换。
### 03.协程：asyncio 操作,asyncio.run 一次开启多个任务，任务的执行效率很高。
### 04.异步操作 模块：aiohttp。项目目标：采用异步操作进行爬取多张图片，思路分析： 1 发送请求 2 得到图片的内容 3 保存到文件。
#### 目标网址：http://kr.shanghai-jiuxin.com/file/2020/1031/small774218be86d832f359637ab120eba52d.jpg 等三张图片，采用异步操作来下载图片。
### 05.异步协程实战：爬取百度小说-西游记，这里使用同步请求与异步请求相结合的方式，
### 相关介绍：
### 1 请求小说的章节和标题只需要请求一次即可，得到所有标签的 cid 采用同步请求即可 requests 模块。
### 2 获取文章的具体内容，采用异步的操作。
#### 目标网址：http://dushu.baidu.com/pc/detail?gid=4306063500 
### 06.异步爬取视频实战，为91网站搜索的相关视频。
### 项目的相关流程为：
### 1.拿到网页的源代码。
### 2.从网页的源代码提取到M3U8的url。
### 3.下载网页的M3U8。
### 4.读取M3U8文件，下载视频。
### 5.合并视频（使用各种手段即可，不仅仅是编程手段：主要是使用软件将片段视频合并成一个整体的视频）。
#### 目标网址：https://www.91kanju.com/vod-play/54812-1-1.html
## 5.Selenium 浏览器模拟
### 01.selenium引入介绍：
### 浏览器的驱动：网址：https://npm.taobao.org/mirrors/chromedriver 默认情况下是谷歌浏览器（根据自己浏览器的版本进行下载，如果没有可以下载上一个版本，把解压好的文件复制到python文件夹下即可
#### 目标网址：https://www.endata.com.cn/BoxOffice/BO/Year/index.html
## 02.Selenium 的各种操作
### 目标流程：
### 1.找到某个元素点击它，这里选用的是xpath。（这里找到的是进去页面看见全国）
### 2.找到搜索框，并在搜索框里面搜索python （有2种方法 直接回车/找到搜索按钮就可以）
####  time.sleep(2)  让浏览器缓一会 可能报错，假如为阿贾克斯请求的话，页面是局部刷新的，让浏览器等一会。
### 3.数据的爬取，最后进行数据的可视化存储。
#### 目标网址：http://www.lagou.com 
## 03.窗口之间的切换
### 相关流程：
### 1.使用 Selenium 模块进行浏览器的模拟登录相关的网页。
### 2.进入网页进行相关信息的提取。（同样子，希望网页不会瞬间的跳转，需要对程序进行睡眠的操作 time.sleep(2)）
### 3.在 Selenium 眼中默认的网址还是原来那个，并不会切换到现在打开的新的网页的地址，所以要进行窗口的切换。
#### 目标网址：http://www.lagou.com 
## 04.无头浏览器
### 无头浏览器相关介绍：让浏览器在后台自己默默的运行即可，最后只是返回数据，不让浏览器进行运作。
### 注意：配置文件是万年不变的代码，不用刻意去记录相关的代码，直接使用即可。（已在代码中进行注释）
#### 目标网址：https://www.endata.com.cn/BoxOffice/BO/Year/index.html 
## 05.超级鹰登录
### 相关介绍：目前来说验证码的处理：
### 1.图像识别（机器来说不太好识别，有些识别不太适用）
### 2.选择互联网上面成熟的验证码破解工具
### 注意事项：需要在 chaojiying = Chaojiying_Client('注册的用户名', '用户密码', '注册码') 进行填写自己相关信息即可。代码已经成为体系，稍微改动即可。最后在官网进行选择合适的验证码类型即可。
#### 超级鹰网站：http://www.chaojiying.com/
## 06.用超级鹰干超级鹰
### 相关介绍：使用超级鹰解决超级鹰的验证码问题
### 1.使用 selenium 模块里面的 webdriver功能对其进行模拟浏览器自动的登录。
### 2.使用 Xpath 进行定位用户名，密码，和验证码，然后向网页源代码中填入相关的信息。（最好使其程序睡眠一段时间）
### 3.最后寻找到登录按钮，进行点击即可。
#### 目标网站：http://www.chaojiying.com/user/login/ 
## 6.WebSpider基础知识讲解
### 本章节为WebSpider基础知识讲解和复习，并且对现有知识进行相应的扩充。具体查看文件夹下的 readme.md 文件。
