import urllib.request
import urllib.request
from bs4 import BeautifulSoup


class LaGouSpider(object):
    # url = 'https://www.lagou.com/beijing-zhaopin/Java/3/'
    url = 'https://www.lagou.com/'

    def __init__(self, place, job, start_page, end_page):
        # 将上面的参数都保存为自己的成员属性
        self.place = place
        self.job = job
        self.start_page = start_page
        self.end_page = end_page

    # 根据 page拼接指定的url,然后生成请求对象
    def handle_request(self, page):
        # for page in range(self.start_page, self.end_page + 1):
        url_now = self.url + self.place + '-zhaopin/' + self.job + '/' + str(page) + '/'
        print(url_now)
        # 构建请求对象化，

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
        }
        requests = urllib.request.Request(url=url_now, headers=headers)
        return requests

    # 解析内容的函数
    def parse_content(self, content):
        # 生成对象
        soup = BeautifulSoup(content, 'lxml')
        # 爬取的思路：先找到所有的li标签，因为一个li就是一个工作的岗位，然后遍历整个li的标签,通过table的select，find方法去寻找每一条记录的具体信息
        print(soup.find_all('li'))
        # new_list = li_list.append()
        # s_position_list > ul > li:nth-child(1)
        # print(new_list)
        # print(len(new_list))

    def run(self):
        # 循环，循环爬取每一页的数据:
        for page in range(self.start_page, self.end_page + 1):
            requests = self.handle_request(page)
            # 发送请求，获取内容
            content = urllib.request.urlopen(requests).read().decode()
            # 解析内容
            self.parse_content(content)


def main():
    place = input('请输入工作地点：')
    job = input('请输入想要的工作：')
    start_page = int(input('请输入开始的页码：'))
    end_page = int(input('请输入结束的页码：'))

    spider = LaGouSpider(place, job, start_page, end_page)
    spider.run()


if __name__ == '__main__':
    main()
