"""
目标网站：http://www.haoduanzi.com/wen/
"""
import re
import urllib.request
import urllib.parse
from lxml import etree
import time
import json  # 保存到文件中

item_list = []


def handle_request(url, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    # url的拼接：基本语法是通过 {} 和 : 来代替以前的 % 。
    url = url.format(page)
    # url = url % page
    # print(url)
    request = urllib.request.Request(url=url, headers=headers)
    return request


def parse_content(content):
    # 生成对象
    tree = etree.HTML(content)
    # 抓取内容
    # 消除class属性，15个li的标签但是会有5ge
    list = tree.xpath('//ul[@class="list-box"]//li[not(@class)]')
    # print(list)
    # print(len(list))
    for a in list:
        # 获取标题
        title = a.xpath('.//div[1]/h2/text()')[0]
        # 获取内容
        text_lt = a.xpath('.//div[@class="content"]/a//text()')
        # print(text_lt)
        text = '\n'.join(text_lt)
        # 去除所有的回车符\r和换行符\n，去除空格，去除\u3000
        text = text.replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
        item = {
            "标题": title,
            "内容": text
        }
        # print(item)
        # 将内容添加到字典中去,append添加的意思，将item添加到字典中去
        item_list.append(item)
        # print(item_list)


def main():
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    # 网页的url必须是http://才可以
    url = 'http://www.haoduanzi.com/category/?1-{}.html'
    # url = 'www.haoduanzi.com/category/?1-%s.html'
    for page in range(start_page, end_page + 1):
        # 获取请求对象
        request = handle_request(url, page)
        # 读取内容
        content = urllib.request.urlopen(request).read().decode('utf-8')  # 编码格式为charset=utf-8
        # 解析内容
        parse_content(content)
        time.sleep(2)

    # 写入文件
    string = json.dumps(item_list, ensure_ascii=False)
    with open('duanzi.txt', 'w', encoding='utf-8') as fp:
        fp.write(string)


if __name__ == '__main__':
    main()
