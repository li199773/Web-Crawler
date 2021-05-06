import urllib.request
import urllib.parse

word = input('请输入国家的名字：')
url = 'http://www.baidu.com/s?'

#参数写成一个字典
data = {
    'ie':'utf-8',
    'wd': word,
}
query_string = urllib.parse.urlencode(data)
url += query_string

# 进行发送请求
resp =urllib.request.urlopen(url)
filename = word + '.html'
# 定义一个，以传入参数生成html文件
with open(filename,'wb') as fp:
    fp.write(resp.read())
