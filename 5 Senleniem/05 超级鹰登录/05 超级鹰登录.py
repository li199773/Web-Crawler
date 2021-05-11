"""
超级鹰网站：http://www.chaojiying.com/
根据代码的提示操作即可

目前来说 验证码的处理：
1.图像识别（机器来说不太好识别，有些识别不太适用）
2.选择互联网上面成熟的验证码破解工具
"""

#!/usr/bin/env python
# coding:utf-8

import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    # 用户中心>>软件ID 生成一个替换 96001
    chaojiying = Chaojiying_Client('li199773', 'li19977312', '915845')
    # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    im = open('code.png', 'rb').read() #im就是图片的所有字节（图片）
    # 1902 验证码类型  官方网站>>价格体系
    print(chaojiying.PostPic(im, 1902))

