# 无头浏览器：让浏览器在后台自己默默的运行即可，最后只是返回数据，不让浏览器进行运作
# 目标网址：https://www.endata.com.cn/BoxOffice/BO/Year/index.html
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
# 该模块是对Chrome浏览器进行配置
from selenium.webdriver.support.select import Select
import time

# 准备好配置文件
# 不用记录，万年不变的代码
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disbale--gpu")


web = Chrome(options=opt) # 把设置好的参数传送给Chrome浏览器

web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")

# 定位到选择年份的标签
sel_li = web.find_element_by_xpath('//*[@id="OptionDate"]')
# 对select进行包装
sel = Select(sel_li)
# 让浏览器进行调整选项
for i in range(len(sel.options)):# i就是每一个下拉菜单的索引位置
    sel.select_by_index(i)
    time.sleep(2)
    tst = web.find_element_by_xpath('//*[@id="TableList"]/table/tbody')
    print(tst.text)
    print("---------------")


print("程序下载完成！！！")
web.close()