"""
目标网址：http://www.chaojiying.com/user/login/
使用超级鹰解决超级鹰的验证码的问题
"""

from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
import time

web = Chrome()

web.get("http://www.chaojiying.com/user/login/")

# 处理验证码
img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
# 后面的代码的意思是将该区域的图片进行截屏保存处理，img此时拿到的是图片的字节，不需要处理即可
chaojiying = Chaojiying_Client('li199773', 'li19977312', '915845')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']

# 向网页的源代码中填入用户名，密码，验证码，然后点击确定即可
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("li199773")
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("li19977312")
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)

time.sleep(5)
# 点击登录
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()


