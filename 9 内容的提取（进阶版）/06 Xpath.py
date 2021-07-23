'''
什么是Xpath?
    首先要了解的是xml:XML 指可扩展标记语言,XML 被设计用来传输和存储数据。
    xml是用来存储和传输数据使用的
    和HTML不用的有两点：
    （1）html是用来显示数据的，xml是用来传输数据的
    （2）html标签是固定的，xml标签是自定义的
    类似以下的形式：标签都是自己定义的
        <note>
        <to>George</to>
        <from>John</from>
        <heading>Reminder</heading>
        <body>Don't forget the meeting!</body>
        </note>

        Xpath用来在xml中查找指定的元素，他是一种路径的表达式
        常用的路径表达式
        //：不考虑位置的查找
        ./:从当前的节点开始向下进行查找
        @:选取属性

        实例：
        /bookstore/book 选取根节点bookstore下面直接子节点book
        //book 选取所有的book
        bookstore//book 选取bookstore下面所有的book
        /bookstore/book[1]	选取属于 bookstore 子元素的第一个 book 元素。
        /bookstore/book[last()]	选取属于 bookstore 子元素的最后一个 book 元素。last()是一个函数
        /bookstore/book[position()<3]	选取最前面的两个属于 bookstore 元素的子元素的 book 元素。position()是位置函数的意思
        //title[@lang]	选取所有拥有名为 lang 的属性的 title 元素。
        //title[@lang='eng']	选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。又进行一次限制
        *	匹配任何元素节点。

        安装Xpath插件：Xpath Helper

以百度为例子：
    1.属性定位：
        // input[ @ type = "text"]  寻找百度的搜索框
        //input[@class="btn self-btn bg s_btn"] 百度文字的搜索按键
    2.层级定位：
        //div[@id="head_wrapper"]/div[1]/div/form[@id="form"]/span[1]/span[2]
        显示的是：按图片搜索
        //div[@id="head_wrapper"]//span[@class="soutu-hover-tip"]
        // 代表的是在跟根目录下面进行寻找所有的span的内容
    3.逻辑运算：
        //input[@class="s_ipt" and @name="wd"]
        可以加上and然后进行更精确的限制查询的标签
    4.模糊匹配
        contains:里面包含这个字符就可以
         //input[contains(@class,"s_i")] 寻找属性为class为 s_ixxx 的标签
        starts-with:必须以这个字符开头才可以进行
         //input[starts-with(@class,"s_i")] 输出结果为一个
    5.取文本
        //div[@id="s-user-name-menu"]/a[4]/text()
    6.取属性
        //div[@id="s-user-name-menu"]/a[2]/@href

    代码中使用Xpath
        from lxml import etree
        两种使用方式：将html文档变成一个对象，然后调用对象的方法去查找指定的节点
        (1)本地文件
        tree = etree.parse(文件名)
        (2)网络文件
        tree = etree.html(网页字符串)
'''

