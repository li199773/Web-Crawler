# 目标网址:https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=
# 豆瓣电影的动作类排行榜
import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

# start=20&limit=20
# start=0&limit=5
# start=1&limit=5
# 经过实验看到start代表从第几个电影开始，每页限制5个电影的输出，start不是页数意思，是显示电影的数量

page = int(input('请输入页数：'))
number = 20

data = {
    'start': (page - 1)*number,
    'limit': number,
}
# 将字典转换成queruy_string
query_string = urllib.parse.urlencode(data)
url += query_string

# 构建请求对象
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}
# 发送请求
requset = urllib.request.Request(url=url, headers=headers)
# 返回请求
response = urllib.request.urlopen(requset)

print(response.read().decode())