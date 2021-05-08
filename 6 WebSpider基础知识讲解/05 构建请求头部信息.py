# 构建请求头部信息（反爬第一步）
# 伪装自己的UA，让服务端认为你是浏览器在上网
import urllib.request
import urllib.parse

url = 'http://www.baidu.com/'
# resp = urllib.request.urlopen(url)
# print(resp.read().decode())
# 这里看到传送的网页信息不全面，所以要进行伪装浏览器

# 伪装头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}
# 构建请求对象
request = urllib.request.Request(url=url,headers=headers)
# 发送请求
response = urllib.request.urlopen(request)# 将请求对象写入即可
print(response.read().decode())
