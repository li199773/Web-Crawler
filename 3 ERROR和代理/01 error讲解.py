"""
# URLError/HTTPError:
NameError，TypeError,FileNotError,异常处理,结构，type-execpt
这两个都在 urllib.error 模块里面，必须先导入这个模块才行
1.URLError问题
（1）没有网
（2）服务器连接失败
（3）找不到指定的服务器
"""
# print(a)
# 运行提示：NameError: name 'a' is not defined，说明 a 未被找到
import urllib.request
import urllib.parse
import urllib.error

#url = 'http://www.maodanan.com'

url = 'https://www.cnblogs.com/yfsm1123/p/1071344.html'

# response = urllib.request.urlopen(url)
# print(response)
# 这里提示失败：urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>

# 用try进行尝试打开，如果有异常进行抛出，用 Execption 进行捕获,最后进行打印即可.
# Execption 是官方给出的异常类，都可以用Execption进行捕获
try:
    response = urllib.request.urlopen(url)
    print(response)
except Exception as e:
    print(e.code)
    # 打印状态码 404
# <urlopen error [Errno 11001] getaddrinfo failed>
# 给提示说打开失败

"""
2.HTTPError：
    是 URLError 的一个子类，也可以通过 URLError 进行捕获
    注意：
    两个都要捕获的时候,需要将HTTPError写到最上面，将URLError写到下面，因为HTTPError是 URLError 的一个子类.
"""