"""
1.post请求讲解：阿贾克斯请求
看 XHR 里面请求头里面有 X-Requested-With 的话就是 post 请求
2.目标网址：https://fanyi.baidu.com/?aldtype=16047#auto/zh 百度翻译 搜索baby
找到 XHR 即可 发现第四个 sug 是目标的网址，使用 www.json.cn 网址进行 json 格式的转换，发现可以进行json格式的转换
3.fiddler 抓包
post请求的话是个小本上面有个向右的箭头
"""
import urllib.request
import urllib.parse

# 获取目标post_url的地址
post_url = 'https://fanyi.baidu.com/sug'
# 构建表单数据，写成一个字典，对字典就行发送请求即可
word = input('请输入查找的英文单词:')
from_data = {
    'kw':word,
}
# 构建请求对象
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'

}
request = urllib.request.Request(url=post_url,headers=headers)
# 发送post请求
query_string = urllib.parse.urlencode(from_data).encode()

resp = urllib.request.urlopen(request,data=query_string)
print(resp.read().decode())

# 练习（进行网页源代码的爬取，拼接网页形式即可）
# post_url = 'https://fanyi.baidu.com/'
# query_string = urllib.parse.urlencode(from_data)
# resp = urllib.request.urlopen(url)
# url = post_url + '?aldtype=16047#en/zh/' +str(from_data)