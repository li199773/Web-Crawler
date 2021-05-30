"""
目标网站：http://www.vipyl.com/article/139/list_1.html
目标分析：1.进入网站之后提取相关语录的标题
        2.然后点击题目之后在提取详细的内容和图片
"""
import urllib.request
import urllib.parse
import re


def handle_request(url, page=None):
    if page != None:
        # 拼接url
        url = url + 'list_' + str(page) + '.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_text(a_href):
    # 调用函数，构建请求对象
    request = handle_request(a_href)
    # 发送请求，获取响应
    content = urllib.request.urlopen(request).read().decode('gbk')
    # print(content)
    # 进行解析详细网页的文字和图片
    pattern = re.compile(r'<p>(.*?)</p>', re.S)
    lt = pattern.findall(content)
    # lt2 = pattern2.findall(content)
    # print(lt)
    # print(lt2)
    # exit()  # 打印出来一次之后就不在进行打印了
    # 在传回的源代码上写一个正则表达式，替换掉全部的图片标签，使其全部消除
    # text = lt[0]
    #     # pattern2 = re.compile(r'<img .*?>')
    #     # text = pattern2.sub('', text)
    return lt


def parse_content(content):
    # 正则表达式进行提取相关联的信息
    pattern = re.compile(r'<b><a href="(/article/\d+/\d+\.html)" target="_blank">(.*?)</a></b>')
    lt = pattern.findall(content)
    # 返回的lt是一个列表，列表中的元素都是元祖，元祖中第一个出现的元素是正则中第一个匹配到的内容，是文章的详细页面的url
    # 第二个内容是正则中匹配到的文章的标题
    # 遍历挣个元祖
    for href_title in lt:
        # 处理全部的详细页面的url和标题
        a_href = 'http://www.vipyl.com/' + href_title[0]
        # print(a_href) 检测拿到的详细页面的url是正确的
        # print(a_href)
        title = href_title[1]
        text = get_text(a_href)
        # 写入html文件中
        string = '<h1>%s</h1>%s' % (title, text)
        with open('雨露文章.html', 'a', encoding='utf-8') as fp:
            fp.write(string)


def main():
    url = 'http://www.vipyl.com/article/139/'
    start_page = int(input('请输入你要开始的页码:'))
    end_page = int(input('请输入你要结束的页码:'))
    for page in range(start_page, end_page + 1):
        # 根据 url 和 page 生成指定的request
        # 对网页进行检查，可以进行请求
        # print(url + 'list_' + str(page) + '.html')
        request = handle_request(url, page)
        # 发送请求
        content = urllib.request.urlopen(request).read().decode('gbk')
        # 解析内容
        parse_content(content)


if __name__ == '__main__':
    main()
