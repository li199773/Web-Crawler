import requests
from lxml import etree

url = "https://jinzhou.zbj.com/search/f/?type=new&kw=saas"
resp = requests.get(url)

html = etree.HTML(resp.text)
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[4]/div[1]/div")
for div in divs:
    price = div.xpath("./div/div[2]/div[2]/i/text()")[0].strip("¥")   #/表示的是根目录下的
    tilte = "saas".join(div.xpath("./div/div[2]/div[3]/a/text()"))# 直接copy找到跟目录即可
    name = div.xpath("./div/div[1]/div[2]/section[1]/h4/a/text()")[0]
    print(tilte)
