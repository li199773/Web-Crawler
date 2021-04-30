"""
1.一般的视频是怎么处理的？
用户上传->转码（把视频处理，2k，1080p,标清）->切片处理（把单个视频进行拆分） 60
解释：用户在拉动进度条的时候可以进行加载 例如一个视频有60个进度条，用户想要观看第45个视频时候，只需要加载相应部分的4 5个视频即可，

2.如何进行操作
需要一个文件的记录：1 文件的播放顺序 2 视频的播放的路径
一般情况下都会存放在M3U文件下（基本都在这个下面） 固定的 像text json 这类的 经过编码之后会变成M3U8

3.想要抓取一个视频的步骤：
    1.找到M3U8文件
    2.找到M3U8文件下的ts文件（各种手段）
    3.可以通过各种手段将ts文件合并成一个mp4文件（各种手段，不仅仅是编程手段）
"""

"""
本项目的流程的：
    1.拿到网页的源代码：url为https://www.91kanju.com/vod-play/54812-1-1.html
    2.从网页的源代码提取到M3U8的url
    3.下载网页的M3U8
    4.读取M3U8文件，下载视频
    5.合并视频

"""

"""
import requests
import re # 提取<script type="text/javascript"> 用re正则表达式就好

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}

obj = re.compile(r"url: '(?P<url>.*?)',",re.S) #提取网页的网址视频的地址 M3U8文件

url = 'https://www.91kanju.com/vod-play/54812-1-1.html'
"""

# 1.解析拿到网页的地址
"""
resp = requests.get(url, headers=headers)
m3u8_url = obj.search(resp.text).group("url") #拿到网页的m3u8的地址
print(m3u8_url)
"""
"""
# 2.解析拿到网页的M3U8的相关文件的代码
resp = requests.get(url, headers=headers)
m3u8_url = obj.search(resp.text).group("url")#拿到网页的m3u8的地址

# print(m3u8_url)
resp.close()

resp2 = requests.get(m3u8_url, headers=headers)

with open("哲仁王后.m3u8",mode="wb") as f:
    f.write(resp2.content)
resp2.close()
print("下载完毕！！！")
"""

#3.解析m3u8文件（首先先把模块注释掉，运行上面的程序的时候首先先把模块引号给删除掉）
import requests

n = 1
with open("哲仁王后.m3u8",mode="r",encoding="utf-8") as f:
    for line in f:
        line = line.strip() #先去掉空格，空白，换行符
        if line.startswith("#"): #如果以#开头，我不要
            continue

#4.下载视频
        resp3 = requests.get(line)
        f = open(f"video/{n}.ts", mode="wb")
        f.write(resp3.content)
        f.close()
        resp3.close()
        n +=1 # 进行循环下载
        print(f"第{n}下载完成!!!") # 说明第几个正在下载完成
#5.最后一步是将所有的视频拼接起来（通过软件进行拼接即可，种类不限，软件很多种类）

# 注意： 这里可能会报黄色警号 尽量把pycharm 分配的资源大一些 调成2048m即可
