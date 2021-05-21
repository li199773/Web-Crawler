# 目标网站：https://www.qiushibaike.com/imgrank/page/1/
# 目标分析：要爬取糗事百科上面的热图的所有的图片

import urllib.request
import urllib.parse
import re
import os
import time


def handle_request(url, page):
    url = url + str(page) + '/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def download_image(content):
    # 写正则表达式进行内容的提取
    # img 的相关格式
    # 会有 img alt 两种格式1
    # <div class="thumb"> 需要在往上再找一级 注意：直接加上<div>的话是找不到的，因为默认的话是在<img>上直接寻找<div>，在网页的源代码上面找不到这样子的排列布局,所以要加上.*?才可以
    # <img src="//pic.qiushibaike.com/system/pictures/12429/124298155/medium/6N7LF17Q211CORQW.jpg" alt="糗事#124298155" class="illustration" width="100%" height="auto">
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" .*?>.*?</div>', re.S)
    # 不需要东西使用 .*? 需要的内容 (.*?)
    # 因为网页的源代码有换行,所以要加上re.S 主要是<'.*?'>不会匹配换行符，加上 re.S 之后合并成单行模式进行正则匹配。
    lt = pattern.findall(content)
    # print(len(lt))
    # 遍历操作
    for image_src in lt:
        image_src = 'http:' + image_src
        # 测试所有的相关网页
        # print(img_src)

        # 创建文件夹，首先要进行判断
        dirname = '糗图'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        # 对图片进行起名字
        filename = image_src.split('/')[-1]
        # 以 / 进行切割，取最后一个为图片的名字
        filepath = dirname + '/' + filename
        # 发送请求，下载图片
        print('第%s图片开始进行下载....' % filename)
        urllib.request.urlretrieve(image_src, filepath)
        print('第%s图片开始结束下载....' % filename)
        # 对网页的请求申请睡眠一会
        time.sleep(1)

def main():
    url = 'https://www.qiushibaike.com/imgrank/page/'
    star_page = int(input('请输入你要开始的页码：'))
    end_page = int(input('请输入你要结束的页码:'))
    for page in range(star_page, end_page + 1):
        print('第%s页开始进行下载....' % page)
        # 1 进行测试打印相关的网页
        # print(url + str(page) +'/')

        # 1.生成请求的对象
        # handle_request 根据不同的 page 产生不同的请求对象
        request = handle_request(url, page)
        # 2.发送请求，获取请求的内容
        content = urllib.request.urlopen(request).read().decode()
        # 3.解析内容，提取相关的图片信息，下载图片
        download_image(content)

        # 打印一下提示，说明代码已经开始开始结束
        print('第%s页开始结束下载....' % page)
        print()
        time.sleep(2)


# 如果是主程序，进行运行的时候的话，就会执行源代码，如果是其他模块进行导入的话就不会进行执行。
if __name__ == '__main__':
    # 1    funtion()
    main()
