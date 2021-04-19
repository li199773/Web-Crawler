#先提取到一个页面的数据
#进行线程池的使用


import requests
from lxml import etree
import csv #写入文件的模块
from concurrent.futures import ThreadPoolExecutor

f = open("data.csv", 'w', encoding="utf-8",newline="")
csvwriter = csv.writer(f)
def download_one_page(url):
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    trs = table.xpath("./tr")[1:]
    for tr in trs:
        txt = tr.xpath("./td/text()")
        # 对数据做简单的处理
        txt = (item.replace("\\", "").replace("/", "") for item in txt)# 一个选择生成器

        csvwriter.writerow(txt)
    print("运行完毕！！！")

"""
# 效率极其低下 单线程操作
if __name__ == '__main__':
    for i in range(1,10):
        download_one_page(f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")
"""

if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(100) as t:
        for i in range(1,100):
            #把任务传给线程池
            t.submit(download_one_page, f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")
    print("全部下载完毕！！！")