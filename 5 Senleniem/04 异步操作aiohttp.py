import asyncio
import aiohttp

urls = [
    "http://kr.shanghai-jiuxin.com/file/2020/1031/small774218be86d832f359637ab120eba52d.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/small563337d07af599a9ea64e620729f367e.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/smalla2c58d6d726fb7ef29390becac5d8643.jpg"
]

async def aiodownload(url):
    # 1 发送请求
    # 2 得到图片的内容
    # 3 保存到文件
    name = url.rsplit("/",1)[1] #从右边切 ，得到1的位置的内容
    async with aiohttp.ClientSession() as session: # async with 意思是不用关闭连接
        async with session.get(url) as resp:  # resp = requests.get()
         # 请求回来了 写入文件
         #可以自己学习一个模块 aiofiles
            with open(name, mode="wb") as f: # 创建文件
                f.write(await resp.content.read()) # 读取的操作是异步的，需要await挂起
                # 如果返回的是网页源代码的话 直接使用resp.text()
        print(name,"完成")

    # s = aiohttp.ClientSession() ==其实就是等于requests.get 或者.post

async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
