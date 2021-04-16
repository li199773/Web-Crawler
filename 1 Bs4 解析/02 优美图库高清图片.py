import requests
from bs4 import BeautifulSoup

headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
        }
url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url=url,headers=headers)
resp.encoding = 'utf-8'

print(resp.text)