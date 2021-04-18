# 找到未加密的参数
# 相办法把参数进行加密（必须参考网易云的加密逻辑），param = encText,encSecKey = encSecKey
# 请求网易并且拿到消息

import requests
from Crypto.Cipher import AES
from base64 import b64decode
import json

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

# 请求方式是POST
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1832088781",
    "threadId": "R_SO_4_1832088781"
}
e = "01001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "SeK9bPTIftfx3u98"

def get_encSecKey():
    return "b27c218ba04a198fcdece8cc7d4389b604e28465366b9ac30dd5549a0d4199437723231f1faa9a558a70fa76544d7f7b4c217c3e42927dd689903bb0942c4ca3841390e05a3479f67d51d70795a882cbdf96fecf89cf1b01a9112daabb1e7f9855d6673abf3827cc59bd14166f7d704239b75395dfbad3f621803a4f7f5d6823"

def get_params(data): #默认这里接受到的是字符串
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second #返回的是params

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def enc_params(data,key): #加密过程
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode('utf-8'), mode=AES.MODE_CBC) #创建加密器
    bs = aes.encrypt(data.encode("utf-8")) #加密,加密的内容的长度必须是16的倍数
    return str(b64decode(bs), "utf-8") #转换成字符串返回


# 处理加密过程
"""
    function b(a, b) { #a 是要加密的内容 b也是秘钥
        var c = CryptoJS.enc.Utf8.parse(b) #？不知道是什么 b是秘钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a) #数据a传给e
          , f = CryptoJS.AES.encrypt(e, c, { #AES是一个加密的算法 C就是秘钥的意思 往回推
            iv: d,  #iv是偏移量
            mode: CryptoJS.mode.CBC # 模式是CBC 差一个秘钥
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) { #d是数据，e是固定的值 01001，f也是固定值 ,g也是固定值
        var h = {} # 空对象
          , i = a(16); #i是一个16位的随机值，把i设置成一个定值
        h.encText = b(d, g),#g是秘钥
        h.encText = b(h.encText, i), #返回的是param i也是秘钥
        h.encSecKey = c(i, e, f), #得到是的encSecKey，e和f是定死的，把i定死就好，此时得到的key就是固定的
        return h
    }
    # 两次加密的结果
    #数据+g传送给b,然后把结果在+i传给b b = params
    #先去找b
    
"""

resp = requests.post(url, data={
        "params": get_params(json.dumps(data)),
        "encSecKey": get_encSecKey()
})
print(resp.text)