"""
Cookie是什么？
    http协议，无状态（每次登录时候的值都不是固定的）
    网站登录的时候就有问题，用来记录用户身份
模拟登录：
    抓包获取cookie，发送请求
"""
import urllib.request
import urllib.parse

# 测试微博 不加上cookie 也返回了相关的信息但是上不去，加上cookie之后可以返回全部的信息。
url = 'https://weibo.com/u/5643259542'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    # 'cookie': 'SINAGLOBAL=7905541055347.778.1619953993537; login_sid_t=b7084b2e5039cdfd1970bd752456ec19; cross_origin_proto=SSL; WBStorage=8daec78e6a891122|undefined; wb_view_log=1536*8641.25; _s_tentry=www.baidu.com; UOR=,,www.baidu.com; Apache=5897599775529.976.1620357450866; ULV=1620357451161:2:2:2:5897599775529.976.1620357450866:1619953993586; SUB=_2A25NkMEODeRhGeNI71ET9SfJzz6IHXVu57XGrDV8PUNbmtAKLWqlkW9NSHl3-xjRaIbbhgZzt1W6R6m5chkue87w; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhTaRBkbKuKZs_pKsiCs01a5JpX5KzhUgL.Fo-cSheESK.fShz2dJLoIp4lK.-LxKqL1-BL12-LxKMLBo.L1h2LxKnLBoqL1h-t; ALF=1651893470; SSOLoginState=1620357470; wvr=6; wb_view_log_5643259542=1536*8641.25; webim_unReadCount=%7B%22time%22%3A1620357824870%2C%22dm_pub_total%22%3A5%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A243%2C%22msgbox%22%3A0%7D',
}
request = urllib.request.Request(url=url, headers=headers, )
response = urllib.request.urlopen(request)
with open('weibo.html', 'wb') as fp:
    fp.write(response.read())
