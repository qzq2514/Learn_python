import time, threading

balance = 0

def change_it(n):
    global balance
    #对余额一加一减
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


'''
我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，
但是，由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。

原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
balance = balance + n
也分两步：
1.计算balance + n，存入临时变量中；
2.将临时变量的值赋给balance。

也就是可以看成：
x = balance + n
balance = x
由于x是局部变量，两个线程各自都有自己的x，当代码正常执行时：
初始值 balance = 0

t1: x1 = balance + 5  # x1 = 0 + 5 = 5
t1: balance = x1      # balance = 5
t1: x1 = balance - 5  # x1 = 5 - 5 = 0
t1: balance = x1      # balance = 0

t2: x2 = balance + 8  # x2 = 0 + 8 = 8
t2: balance = x2      # balance = 8
t2: x2 = balance - 8  # x2 = 8 - 8 = 0
t2: balance = x2      # balance = 0

结果 balance = 0
但是t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：

初始值 balance = 0

t1: x1 = balance + 5  # x1 = 0 + 5 = 5

t2: x2 = balance + 8  # x2 = 0 + 8 = 8
t2: balance = x2      # balance = 8

t1: balance = x1      # balance = 5
t1: x1 = balance - 5  # x1 = 5 - 5 = 0
t1: balance = x1      # balance = 0

t2: x2 = balance - 8  # x2 = 0 - 8 = -8
t2: balance = x2      # balance = -8

结果 balance = -8
'''