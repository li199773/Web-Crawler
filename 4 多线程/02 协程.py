import time
def fun():
    print("我爱赵雪")
    time.sleep(3)
    print("我最爱赵雪")

if __name__ == '__main__':
    fun()

#input()程序也是一种阻塞状态
#request.get(bilibili)在未传送到网页之前，程序也是阻塞的
#一般情况下，IO操作也是一种阻塞的情况

# 协程：协程是当任务阻塞的情况下，会自动的切换成未阻塞的任务上。
# 在宏观上是多任务一起在执行
# 在微观上是看是一个任务一个任务在切换
# 多任务切换 异步操作