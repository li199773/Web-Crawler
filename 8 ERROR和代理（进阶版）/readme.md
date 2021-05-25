# 本章节主要讲解 `error` 和 模拟浏览器登录时的 `headler` 相关的一些列操作。
## 01 `error` 讲解
### 相关介绍：`Error` 主要分为 `URLError` 和 `HTTPError`
### 1.这两个都在 urllib.error 模块里面，必须先导入这个模块才行。
    import urllib.error
### 2.1.URLError问题
#### （1）没有网。
#### （2）服务器连接失败。
#### （3）找不到指定的服务器。
