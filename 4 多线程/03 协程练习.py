import asyncio
import time
#1
"""
async def fun():
    print("我爱中国货")

if __name__ == '__main__':
    g = fun()
    asyncio.run(g) # 需要asynico模块的支持
""" #代码整体测试这个模块的意思

"""
async def fun1():
    print("我爱NIKE")
    time.sleep(2) #当程序出现同步的操作的时候，一异步操作就会停止
    print("我爱NIKE")
async def fun2():
    print("我爱李宁")
    time.sleep(3)
    print("我爱李宁")
async def fun3():
    print("我爱特步")
    time.sleep(4)
    print("我爱特步")

if __name__ == '__main__':
    f1 = fun1()
    f2 = fun2()
    f3 = fun3()

    tasks = [
        f1, f2, f3
    ] # 创建一个列表 ，装入全部的任务
    t1 = time.time()
    asyncio.run(asyncio.wait(tasks)) #一次性开启多个任务
    t2 = time.time()
    print(t2 - t1)
"""
# 还是一个同步代码，没有实现异步的操作

#2
"""
async def fun1():
    print("我爱NIKE")
    await asyncio.sleep(2) #异步操作的代码，进行挂起，先去别的地方睡眠的操作，先去别的地方睡眠
    #time.sleep(2)
    print("我爱NIKE")
async def fun2():
    print("我爱李宁")
    await asyncio.sleep(3)
    #time.sleep(3)
    print("我爱李宁")
async def fun3():
    print("我爱特步")
    await asyncio.sleep(4)
    #time.sleep(4)
    print("我爱特步")

if __name__ == '__main__':
    f1 = fun1()
    f2 = fun2()
    f3 = fun3()

    tasks = [
        f1, f2, f3
    ] # 创建一个列表 ，装入全部的任务
    t1 = time.time()
    asyncio.run(asyncio.wait(tasks)) #一次性开启多个任务
    t2 = time.time()
    print(t2 - t1) #程序开启了异步操作 时间就是最长的那一点加上一点点开启的操作 执行的效率很高，比之前的高很多
# python一般不这么写
"""

#3
async def fun1():
    print("我爱NIKE")
    await asyncio.sleep(2) #异步操作的代码，进行挂起，先去别的地方睡眠的操作，先去别的地方睡眠
    #time.sleep(2)
    print("我爱NIKE")
async def fun2():
    print("我爱李宁")
    await asyncio.sleep(3)
    #time.sleep(3)
    print("我爱李宁")
async def fun3():
    print("我爱特步")
    await asyncio.sleep(4)
    #time.sleep(4)
    print("我爱特步")

async def main():
    tasks = [
        fun1(),
        fun2(),
        fun3()
    ]
    await asyncio.wait((tasks))

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())  # 一次性开启多个任务
    t2 = time.time()
    print(t2 - t1)