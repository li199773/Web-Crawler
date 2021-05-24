## 01 `ajax_get` 请求介绍
### 相关介绍：练习豆瓣电影的阿贾克斯请求的 get 请求。
### 使用 `parse` 将字典转换成 `queruy_string`，然后在进行拼接。
#### 目标网址:https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=& 
## 02 `ajax_post` 请求介绍
### 相关介绍：
### 1.传入参数，可以自定义城市
### 2.通过参数传入网页中
        form_data = {
            'cname': city,
            'pid': '',
            'pageIndex': page,
            'pageSize': size, # 只要是参数，一般情况下都是字符串，最好加上''
        }
### 3.使用`urllib.request`进行网页的拼接。
#### 目标地址：http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname 
## 03 `ajax`贴吧（复杂GET的练习）
### 项目的需求：输入输入吧名，输入起始页码，输入结束页码，然后在当前文件夹下面创建一个以吧名字的文件夹，里面是每一页的html内容,文件名字是以 吧_page.html。
### 观察发现：kw=为你要搜索的吧名字，pn=为显示的数目，可以通过（页数-1）*50， 
        ba_name = input('请输入你要查找的吧名：')
        start_page = int(input('请输入开始的页数：'))
        end_page = int(input('请输入结束的页数：'))  # 数字 字符串类型，加上int()
#### 目标网址：https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150  
