"""
目标网址：https://kyfw.12306.cn/otn/resources/login.html
"""

from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.action_chains import ActionChains
import time

# 初始化超级鹰
chaojiying = Chaojiying_Client('li199773', 'li19977312', '915845')

web = Chrome()
web.get("https://kyfw.12306.cn/otn/resources/login.html")
# 打开网页有些慢，需要让程序简单的睡眠2秒即可
time.sleep(2)
# 页面打开之后默认的是扫码登录，要切换到用户名和密码那一栏
web.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
# 在简单的睡眠3秒左右，验证码加载有些缓慢
time.sleep(3)

# 1.首先处理验证码
verify_element_img = web.find_element_by_xpath('//*[@id="J-loginImg"]')
# 后面的代码的意思是将该区域的图片进行截屏保存处理，img此时拿到的是图片的字节，不需要处理即可

# 用超级鹰识别验证码
dic = chaojiying.PostPic(verify_element_img.screenshot_as_png, 9004)
# 根据超级鹰的官网代码来，9004代表的是返回4个坐标，因为12306的验证码我们需要知道相关信息的坐标进行点击即可
reult = dic['pic_str']
# print(reult) 此时输出的是位置坐标 拿到的坐标类似：95，56|65,23
re_list = reult.split("|")  # 以 | 为界限进行数据的分割
for re in re_list:
    re_temp = re.split(",")  # 然后再以逗号继续进行分割，分成数字的形式，例如：“65” “32"
    x = int(re_temp[0])
    y = int(re_temp[1])
    # 让鼠标指向刚刚获取到的 x,y坐标，然后鼠标点击即可
    # 先把验证码那一栏进行定位，然后以这一栏为基准进行鼠标的偏移量
    ActionChains(web).move_to_element_with_offset(verify_element_img, x, y).click().perform()
    # perform的意思是任务开始执行，任务开始提交！！！
