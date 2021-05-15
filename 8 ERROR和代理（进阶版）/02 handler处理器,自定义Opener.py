"""
Handler处理器，自定义Opener
    urlopen() 给一个请求头，发送请求对象，获取相应
    Request() 定制响应头，创建响应对象
    高级功能：使用代理，Cookie
"""
import urllib.request
import urllib.parse

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}
# 创建一个handler
handler = urllib.request.HTTPHandler()
# 创建一个Opener()
# opener是一个对象，一会发送请求的时候，直接使用opener里面的方法即可，不用使用urlopen了
Opener = urllib.request.build_opener(handler)

# 构建请求对象
request = urllib.request.Request(url=url,headers=headers)
# 发送请求
response = Opener.open(request)
# 使用Opener.open进行打开网页
print(response.read().decode())