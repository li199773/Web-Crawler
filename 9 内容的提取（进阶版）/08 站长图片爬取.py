"""
目标网站：https://sc.chinaz.com
项目需求：爬取站长网站的相关图片，首先获取全部的图片类型，根据用户输入的图片类型进行图片的爬取
"""
import requests
from lxml import etree
import time
import socket
import os

url = "https://sc.chinaz.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Cookie': 'BAIDU_SSP_lcr=https://www.baidu.com/link?url=bnh8KIDb4qGqyTnJ9xwkrQYXsO6h-KWcrhf1hT9Zv_72VVOnEkBko76YKfFjHLdN&wd=&eqid=c03d09f2002d5e4d00000002611226c5; Hm_lpvt_aecc9715b0f5d5f7f34fba48a3c511d6=1628579529; Hm_lvt_aecc9715b0f5d5f7f34fba48a3c511d6=1628579529; UM_distinctid=17b2ee7803de28-0749c8854966db-4343363-e1000-17b2ee7803ecd4; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1628579534; __gads=ID=78b1ccbb604f0885-222680e0bfca0051:T=1628579544:RT=1628579544:S=ALNI_MawNYjFebpTcYIkZPHaAtDOr1B1Ow; CNZZDATA300636=cnzz_eid%3D2076946985-1628577216-%26ntime%3D1628646148; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1628648394'
}


class Zhanzhang:
    def __init__(self, name, start_page, end_page):
        self.name = name
        self.start_page = start_page
        self.end_page = end_page

    def run(self, name_pinyin_whole, url_name):
        # print(name_pinyin_whole)
        # 循环遍历每一页的数据:
        for page in range(self.start_page, self.end_page + 1):
            if page == 1:
                url_name_whole = url_name
            else:
                url_name_whole = url + name_pinyin_whole + '_' + str(page) + '.html'
            # print(url_name_whole)
            self.analysis_image(url_name_whole)

    # 文件解析
    def analysis_image(self, url_name_whole):
        content = requests.get(url=url_name_whole, headers=headers)
        tree2 = etree.HTML(content.text)
        img_list = tree2.xpath('//div[@id="container"]/div/div/a/img/@src2')
        # 懒加载的问题,使用src2使用即可
        dirpath = "站长图片"
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
        for img in img_list:
            img_url = "https:" + img
            # print(img_url) # https://scpic.chinaz.net/Files/pic/pic9/202107/apic34388_s.jpg
            self.download_img(dirpath, img, img_url)

    # 文件下载
    def download_img(self, dirpath, img, img_url):
        file_name = os.path.basename(img)
        # print(file_name)
        # apic34388_s.jpg
        filepath = os.path.join(dirpath, file_name)
        # print(filepath)
        # 站长图片\apic34388_s.jpg
        # 发送请求,保存图片
        resp_img = requests.get(url=img_url, headers=headers)
        with open(filepath, 'wb') as fp:
            fp.write(resp_img.content)
        print("{}下载完成".format(file_name))


def picture_page(name):
    href = tree.xpath('//a[@title="{}"]/@href'.format(name))
    # print(href) # ['/tupian/ribenmeinv.html']
    name_pinyin = href[0].split('.')
    name_pinyin_whole = name_pinyin[0]
    # print(name_pinyin) # ['/tupian/ribenmeinv', 'html']
    # print(name_pinyin_whole)
    url_name = url + href[0]
    # print(url_name)
    resp_picture_file = requests.get(url=url_name, headers=headers)
    tree1 = etree.HTML(resp_picture_file.text)
    all_page = tree1.xpath('//div[@class="fenye"]/a[last()-1]/b/text()')[0]
    # print(all_page)
    print("{}最大页面为{}页".format(name, all_page))
    return name_pinyin_whole, url_name


def main():
    name = input('请输入爬取图片类型名称：')
    name_pinyin_whole, url_name = picture_page(name)
    start_page = int(input('请输入开始的页码：'))
    end_page = int(input('请输入结束的页码：'))
    zhanzhang_spider = Zhanzhang(name, start_page, end_page)
    zhanzhang_spider.run(name_pinyin_whole, url_name)


def first():
    resp = requests.get(url=url + "/tupian", headers=headers)
    resp.encoding = 'utf-8'
    socket.setdefaulttimeout(30)
    global tree
    tree = etree.HTML(resp.text)
    lists = tree.xpath('//div[@class="mt10 feilei"]/div')

    for list in lists:
        picture_name_list = list.xpath("./a/text()")
        print(picture_name_list)
        # for picture_name in picture_name_list:
        #     print(picture_name)
    main()


if __name__ == '__main__':
    first()
