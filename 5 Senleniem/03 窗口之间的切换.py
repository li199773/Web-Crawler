"""
1.窗口之间的切换
2.目标网址：http://www.lagou.com

"""

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()

web.get("http://www.lagou.com")
web.find_element_by_xpath('//*[@id="cboxClose"]').click()
time.sleep(1)
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python",Keys.ENTER)
time.sleep(1)

web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()
# 这时一定会打开一个新窗口 如何进入新窗口进行相关信息的提取
# 在selenium眼中默认的网址还是原来那个，并不会切换到现在打开的新的网页的地址，所以要进行窗口的切换
web.switch_to.window(web.window_handles[-1])# -1代表的是最后一个窗口的意思，可以进行更改

job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)

web.close()
# 关闭现在的网页
web.switch_to.window(web.window_handles[0])
# 让selenium回到原有的网页
print(web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').text)
#这时打印的不只是详情信息还有岗位的信息
