"""
目标网址：https://kyfw.12306.cn/otn/resources/login.html
"""

from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

# 初始化超级鹰
chaojiying = Chaojiying_Client('li199773', 'li19977312', '915845')


# 见代码第58行
# 如果你的程序被识别到了怎么办？（此时分2种情况进行分析）
# 1.Chrome浏览器的版本号小于88（在浏览器的帮助里面查看自己的版本号即可），在你启动浏览器的时候，先向网页嵌入js代码，去掉webdriver
# 相关代码如下：（代码不用记录）：
# web = Chrome()
#
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",{
#     "source":"""
#     navigator.webdriver = undefined
#     Object.defineProperty(navigator,'webdriver',{
#         get : () => undefined
#     })
#     """
# web.get(xxxxxxx)

# 2.Chrome的版本号大于等于88（基本上都在88以上）引入option（同样代码也不用记忆，都是固定的,不用记忆）
# option = Options()
# option.add_experimental_option('excludeSwitches',['enable-automation'])
# option.add_argument('--disable-blink-features=AutomationControlled')
# web = Chrome(options = option)

#option = Options()
# option.add_experimental_option('excludeSwitches',['enable-automation'])
# 这一句话无所谓，相加就加
#option.add_argument('--disable-blink-features=AutomationControlled')
#web = Chrome(options=option)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
   # "Cookie": "JSESSIONID=6F156D09BA0893DC93168BF8BAC9643D; RAIL_EXPIRATION=1619674586480; RAIL_DEVICEID=CU0oorCOIbTEpwC3RSQSYriSyxTb7vGIe7Q_nW7vcAG5URUsrUtuXpxA-UAAocuCf1iWyu0-EtiEwCitEUJhByrQwa90I6_davD9gVQUJoeGRk421ZxP2uz0FUfDKnWGTnnUOdt9Au6rR9BV13JgVcsD4VEUyp_p; BIGipServerpassport=904397066.50215.0000; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=1624834314.64545.0000"
}
web = Chrome()

web.get("https://kyfw.12306.cn/otn/resources/login.html")
# 打开网页有些慢，需要让程序简单的睡眠2秒即可
time.sleep(2)
# 页面打开之后默认的是扫码登录，要切换到用户名和密码那一栏
web.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
# 在简单的睡眠3秒左右，验证码加载有些缓慢
time.sleep(3)

#1.首先处理验证码
verify_element_img = web.find_element_by_xpath('//*[@id="J-loginImg"]')
# 后面的代码的意思是将该区域的图片进行截屏保存处理，img此时拿到的是图片的字节，不需要处理即可

#用超级鹰识别验证码
dic = chaojiying.PostPic(verify_element_img.screenshot_as_png, 9004)
# 根据超级鹰的官网代码来，9004代表的是返回4个坐标，因为12306的验证码我们需要知道相关信息的坐标进行点击即可
reult = dic['pic_str']
# print(reult) 此时输出的是位置坐标 拿到的坐标类似：95，56|65,23
re_list = reult.split("|")# 以 | 为界限进行数据的分割
for re in re_list:
    re_temp = re.split(",") #然后再以逗号继续进行分割，分成数字的形式，例如：“65” “32"
    x = int(re_temp[0])
    y = int(re_temp[1])
    # 让鼠标指向刚刚获取到的 x,y坐标，然后鼠标点击即可
    # 先把验证码那一栏进行定位，然后以这一栏为基准进行鼠标的偏移量
    ActionChains(web).move_to_element_with_offset(verify_element_img,x,y).click().perform()
    # perform的意思是任务开始执行，任务开始提交！！！

# 最好让程序睡眠2秒左右
time.sleep(2)
# 请求输入用户名和密码
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys('123456')
# 输入自己用户名
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('123456')
# 输入自己的密码

# 点击登录
web.find_element_by_xpath('//*[@id="J-login"]').click()

"""
# 此时出现温馨提醒：必须让拖动进度条在进行完成检测，因为检测到是模拟浏览器进行登录的，是一直登录不上去的
在Console界面下输入 window.navigator.webdriver 会提示是ture,在原页面下出现的应该是false才对，加上前文的代码后会变成false
"""

# 拖拽验证码那个进度条即可
time.sleep(5)
# 睡眠的时间尽量长一些
btn = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn,300,0).perform()