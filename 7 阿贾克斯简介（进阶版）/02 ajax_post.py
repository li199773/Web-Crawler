import urllib.request
import urllib.parse

# 首先获取目标的网址
post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
# 传入参数，可以自定义城市
city = input('请输入你要查找城市：')
page = input('请输入你要查找的页数：')
size = input('请输入你要多少个：')
# 通过参数传入网页中
form_data = {
    'cname': city,
    'pid': '',
    'pageIndex': page,
    'pageSize': size, # 只要是参数，一般情况下都是字符串，最好加上''
}
# 伪装成浏览器发送
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'

}
# 构建请求头部
request = urllib.request.Request(url=post_url,headers=headers)
# 将上述form_data进行网页的拼接
form_data = urllib.parse.urlencode(form_data).encode()
# 对目标网页发送请求，返回相应的数据
response = urllib.request.urlopen(request,data=form_data)
# 打印相关的信息
print(response.read().decode())