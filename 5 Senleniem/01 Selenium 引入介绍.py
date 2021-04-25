"""
网页地址：https://www.endata.com.cn/BoxOffice/BO/Year/index.html
打开后发现 Preview 里面全是乱码
里面全是乱码，需要进行解密操作，但是太过于复杂，想法是通过网页浏览器进行解密，然后再进行提取信息即可。
引入selenium模块 自动化测试工具；功能：打开浏览器，像人一样去操作浏览器，然后从中去提取相关的信息
环境的搭建：
1.pip install selenium
2.浏览器的驱动：网址：https://npm.taobao.org/mirrors/chromedriver 默认情况下是谷歌浏览器
相关的版本号要对应上，对应不上就找上一个版本的就可以
把解压好的文件复制到python文件夹下即可
进行测试让selenium启动谷歌浏览器
"""
# 测试： 让selenium启动chrome浏览器
from selenium.webdriver import Chrome
#1.创建浏览器
web = Chrome()
#2.使用selenium打开浏览器的网址
web.get("http://www.baidu.com")

print(web.title) # title 就是网页的标题
