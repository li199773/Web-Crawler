# 本章节主要讲解 `error` 和模拟浏览器登录时的 `headler` 相关操作
## 01 `error` 讲解
### 相关介绍：`Error` 主要分为 `URLError` 和 `HTTPError`
### 1.这两个都在 urllib.error 模块里面，必须先导入这个模块才行。
    import urllib.error
### 2.`URLError`问题
#### （1）没有网。
#### （2）服务器连接失败。
#### （3）找不到指定的服务器。
### 3.`HTTPError`：是 `URLError` 的一个子类，也可以通过 `URLError` 进行捕获
#### 注意：两个都要捕获的时候,需要将`HTTPError`写到最上面，将 `URLError` 写到下面，因为`HTTPError`是 `URLError` 的一个子类。
## 用try进行尝试打开，如果有异常进行抛出，用 Execption 进行捕获,最后进行打印即可。
## Execption 是官方给出的异常类，都可以用Execption进行捕获。
    try:
        response = urllib.request.urlopen(url)
        print(response)
    except Exception as e:
        print(e.code)
#### 目标网址：https://www.cnblogs.com/yfsm1123/p/1071344.html 
## 02 `Handler`处理器，自定义`Opener`
### 相关介绍：Handler处理器，自定义Opener
### 1.`urlopen()` 给一个请求头，发送请求对象，获取相应。
### 2.`Request()` 定制响应头，创建响应对象。
### 3.高级功能：使用代理，Cookie。
#### 目标网址：http://www.baidu.com 
## 03 代理
### 主要讲解了什么是代理，在程序中如何进行代理以及我们如何进行代理的相关的配置。
### 相关具体介绍见代码文件。
## 04 `Cookie` 介绍
### 主要讲解了`Cookie`是什么？以及`Cookie`的相关练习。
### 1.http协议，无状态（每次登录时候的值都不是固定的）。
### 2.网站登录的时候就有问题，用来记录用户身份。
