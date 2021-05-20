"""
为什么会引入正则表达式?
    用来匹配一类相同规则的字符串（像所有的邮箱，所有手机号码）
    主要的功能：
        1.正则替换
        要把所有的邮箱删除，我们可以用正则替换，把邮箱替换空。
        2.正则匹配
        来匹配到指定的邮箱
    规则：
        单字符：
            .:除换行之外所有的字符
            []：[aoe] a 到 e 之间任意一个，是任意一个
            \d：数字 [0-9]
            \D：非数字
            \w：数字 字母 下换线 中文
            \W：非\w
            \s：所有的空白字符
            \S：非空白字符
        数量修饰：
            *:任意多次，也可以是 >=0
            +:至少一次 >=1
            ?:可有可无  0次或者一次
            {m}:固定一次
            {m,}:至少一次
            {m,n}:m-n次
        边界：
            ^：以某某开头
            $：以某某结尾
        分组：
            (){4}  视为一个整体；例：ca(4)是对a进行请求3次，要是想对ca进行请求3次的话，要对其进行（）处理。
            () 确定优先级 确定子模式
        贪婪模式：
            .*?:
            .+?:
            re.I:忽略大小写
            re.M:多行匹配
            re.S:单行匹配

            match:是从开头开始寻找
            search:是从任意的位置开始寻找，第一个没有寻找到的话开始从第二个开始进行寻找
            findall:寻找全部的所有的
            re.sub(正则表达式，想要替换的内容，字符串)
"""
# 子模式的例子
import re

string = '<p><div><span>猪八戒</span></div></p>'
pattern = re.compile(r'<(\w+)><(\w+)>\w+</\2></\1>')
ret = pattern.search(string)
print(ret)
# 贪婪模式的例子：
string1 = '<div>猪八戒</div></div></div>'
pattern1 = re.compile(r'<div>.*?</div>')
ret1 = pattern1.search(string1)
print(ret1)
# 多行匹配的例子；
string2 = '''hate is a beautifil fell
love you very much
love he
love she
'''
prttern2 = re.compile(r'^love', re.M)
ret2 = prttern2.search(string2)
ret3 = prttern2.findall(string2)
print(ret2)
print(ret3)
# 结果是None 匹配失败
# 加上re.M之后可以匹配到：结果是 <re.Match object; span=(25, 29), match='love'>
# 要想匹配全部的love 需要把 search 换成 findall 即可 结果是 ['love', 'love', 'love']

# 多行匹配例子2：
string3 = """<div>沁园春-雪
北国风光
千里冰封
万里雪飘
望长城内外
惟余莽莽
大河上下
顿时滔滔
山舞银蛇
原驰蜡象
欲比天公试比高
</div>
"""
prttern3 = re.compile(r'<div>(\w+)</div>', re.S)
ret4 = prttern3.findall(string3)
print(ret4)
# prttern3 = re.compile(r'<div>(\w+)</div>', re.S)
# (\w+) 这个话没有办法进行匹配，因为会有换行符

prttern4 = re.compile(r'<div>(.*)</div>', re.S)
ret5 = prttern4.findall(string3)
print(ret5)

# 正则替换的例子:
string4 = 'i love you,you do not love me.'
prttern5 = re.compile(r'do not love')
# 两种方法都可以，看自己喜欢哪一种即可
ret6 = prttern5.sub('love', string4)
ret7 = re.sub(r'do not love', 'hate', string4)
print(ret6)
print(ret7)


# 传递参数的例子：
# 目标：想要把175减去10传回然后再把女孩替换成男孩
def fun(a):
    # print(a)
    ret9 = int(a.group())
    # print(ret9)
    return str(ret9 - 10)

string8 = '我喜欢身高为175的女孩'
pattern8 = re.compile(r'\d+')
ret8 = pattern8.sub(fun, string8)
ret9 = re.sub(r'女孩', '男孩', ret8)
print(ret8)
# 再将传递参数生成的话语在传递给 ret9 进行替换：将女孩替换成男孩即可
print(ret9)
