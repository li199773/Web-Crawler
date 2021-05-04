"""
url 只能由特定的字符组成，字母，数字，下划线
如果出现其他的，比如￥ 空格 中文等，就要对其进行编码
url.parse
.quote:解码函数,将中文转换成%xxx
.unquote:编码函数,将%xxx转化成指定的字符
.unlencode:给一个字典，将字典拼接成query_string,并且实现自动编码的功能，（有些网址中不能出现非法的字符 ）
"""
import urllib.parse

# image_url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi.serengeseba.com%2Fuploads%2Fi_4_2475446966x1356278756_26.jpg&refer=http%3A%2F%2Fi.serengeseba.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1622273715&t=6af6c1555229cdc7c4c5b4b668ce203a'
#
# url = 'http://www.baidu.com/index.html?name=中国&pwd=123456'
# # url进行解码，不然访问失败，因为有网页不识别的符号
# reture = urllib.parse.quote(url)
# # 进行编码
# re = urllib.parse.unquote(reture)
# print(re)

#.unlencode:相关介绍
url = 'http://www.baidu.com/'
# url = 'http://www.baidu.com/index.html?name=中国&age=18&height=180&sex=nv&weight=180'
# 如何拼接成上述的url网址
name = '中国'
age = '18'
height = '180'
sex = 'nv'
weight = '180'
data = {
    'name': name,
    'age': age,
    'sex': sex,
    'height': height,
    'weight': weight,
}
# 遍历字典 一般情况下需要自己写
# 先来一个空的列表
# lt = []
# for k, v in data.items():
#     lt.append(k + '=' + str(v))
# query_string = '&'.join(lt)
# 相关网站的拼接会经常使用

# 但是在parse中已经封装好了相关的代码
query_string = urllib.parse.urlencode(data)
# 参数必须是字典的形式
print(query_string)
url = url + '?' + query_string
print(url)
