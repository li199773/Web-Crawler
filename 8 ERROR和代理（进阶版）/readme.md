# 本章节主要讲解 `error` 和 模拟浏览器登录时的 `headler` 相关的一些列操作。
## 01 `error` 讲解
### 相关介绍：`Error` 主要分为 `URLError` 和 `HTTPError`
### 1.这两个都在 urllib.error 模块里面，必须先导入这个模块才行。
    import urllib.error
### 2.`URLErro`r问题
#### （1）没有网。
#### （2）服务器连接失败。
#### （3）找不到指定的服务器。
### 2.`HTTPError`：是 `URLError` 的一个子类，也可以通过 `URLError` 进行捕获
#### 注意：两个都要捕获的时候,需要将`HTTPError`写到最上面，将 `URLError` 写到下面，因为`HTTPError`是 `URLError` 的一个子类.
