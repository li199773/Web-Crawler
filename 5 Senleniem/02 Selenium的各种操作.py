# 目标网址：http://www.lagou.com

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()

web.get("http://www.lagou.com")
# 1.找到某个元素点击它，这里选用的是xpath
# 这里找到的是进去页面看见全国
le = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
# le =web.find_elements_by_class_name() elemennts 有s表示的是找到页面全部的，没有s的话表示只是
# 寻找第一个即可

le.click() # 这时浏览器会自动点击它

#2.找到搜索框，并在搜索框里面搜索python （有2中方法 直接回车/找到搜索按钮就可以）

time.sleep(2) #让浏览器缓一会 可能报错，假如为阿贾克斯请求的话，页面是局部刷新的，让浏览器等一会
ss = web.find_element_by_xpath('//*[@id="search_input"]').send_keys("西安",Keys.ENTER)
# 这时直接回车的代码，需要导入Keys模块，让浏览器可以自动敲击回车

#3.进行数据的爬取
"""
使用selenium之后，进行数据的爬取，首先先找到目标的li即可，使用xpath copy即可
"""
list_li = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')#找的是一堆得ls 用s
for li in list_li:
    name = li.find_element_by_xpath("./div[1]/div[1]/div[1]/a/h3").text
    # 另一种写法：name = li.find_element_by_tag_name("h3").text
    # 一定要注意.text ？？？
    gongzi = li.find_element_by_xpath("./div[1]/div[1]/div[2]/div/span").text
    company_name = li.find_element_by_xpath("./div[1]/div[2]/div[1]/a").text
    print(company_name,name, gongzi)