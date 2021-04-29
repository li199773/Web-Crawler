# 网站的源代码是http://dushu.baidu.com/pc/detail?gid=4306063500


# 1 得到所有章节的名称和标题 包括名称和cid
# http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}
# 2 得的小说的具体章节的内容
# http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo%":1}

# 分析程序的流程：
# 1 时请求到的小说的章节和标题只需要请求一次就好，得到所有标签的cid 采用同步请求即可 requests
# 2 时获取文章的具体内容，采用异步的操作

import requests
import asyncio
import aiohttp
import aiofiles # 异步存取的模块 就是写入文件的意思
import json
"""
1.同步操作：访问getCatalog 拿到所得名称和章节的cid
2.异步操作：访问getChapterContent 下载所有文章的内容
"""
async def aiodownload(cid,b_id,title):
    data = {
        "book_id":b_id,
        "cid":f"{b_id}|{cid}",
        "need_bookinfo%": 1
    }
    data = json.dumps(data)
    url = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()

            async with aiofiles.open(title,mode="w",encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content']) # 把小说的内容写入文档中

async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']: #item 对应的是每个章节的名称和cid
        title = item['title']
        cid = item['cid']
        # 准备异步的任务 每一个cid就是一个异步任务 获取每个章节的所有的文章

        tasks.append(aiodownload(cid,b_id,title))

    await asyncio.wait(tasks)

if __name__ == '__main__':
    b_id = "4306063500"
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + b_id + '"}'
    asyncio.run(getCatalog(url))

