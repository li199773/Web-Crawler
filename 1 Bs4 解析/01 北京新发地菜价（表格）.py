import requests
from bs4 import BeautifulSoup
import csv


url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp = requests.get(url)
f = open("菜价.csv", 'a', encoding='utf-8')
csvwiter = csv.writer(f)

page = BeautifulSoup(resp.text, "html.parser")
table = page.find("table", class_="hq_table")   #class属性（id等等也有）有下划线 注意
trs = table.find_all("tr")[1:] #在表格中找到所有的行
for tr in trs:
    tds = tr.find_all("td")
    name = tds[0].text
    low = tds[1].text
    avg = tds[2].text
    high = tds[3].text
    guige = tds[4].text
    danwei = tds[5].text
    date = tds[6].text

    csvwiter.writerows([name,low,avg,high,guige,danwei,date])

f.close()
print("over!!!")







