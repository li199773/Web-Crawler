"""
题外话：在Pycharm软件下显示多个工程，在建立新的工程文件时需要点击Attach按钮
"""
"""
网页知识一栏：
1.学会使用浏览器进入开发者工具进行网页信息的抓包：
All:网页的所有信息（一般情况下选中all即可）
XHR:阿贾克斯（ajax）请求
js:一个网页有很多个js文件
img:网页的图片信息

右键开发者工具：Network
    右边栏：显示详细的信息：request headers response 
    query string:get参数 
    from data:post参数
专业抓包软件的使用：fiddler
1.配置:tools==>options==>https
    选中:capture https
        decrypt https trafic
        ignore xxx
    点击右边的action，信任根证书
    配置完毕，fiddler重启即可
2.抓包
    <>：html请求的内容
    {json}:（需要格外的注意）json数据，很有可能是个接口
    {js}.{css}就不在过多的介绍
    
    停止抓取：file==>capture 点击就会切换
    点击请求，右边选中 Inspectors(窗口分为右上和右下)
    右上：显示的请求信息，默认为Headers，点击
        Raw：请求头的详细信息(最有价值的信息，请求头在这里面)
        webforms:请求所带的参数，query_string,formdata
    右下：http显示的相应信息
        点击黄色进度条进行解码（有些代码是被压缩的）
        raw：响应的所有信息
        headers:响应头
        json:接口返回的内容（有些请求是阿贾克斯请求）
    左下黑色框：输入指令来快捷进行指令：
        clear:清除所有的请求
        select json：快速选择所有的json请求
        select image：快速选择所有的图片请求
        ?内容：搜索所有带内容的所有请求
        
        点击enter即可  


一般情况下，使用Chrome浏览器的开发者工具即可解决
"""