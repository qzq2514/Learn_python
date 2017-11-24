import time, threading

balance = 0
#之前ThreadProblem.py中存在的线程访问同变量出现的问题，归结原因就是修改balance时有好几条语句，随时可能
#被别的线程打断，从而导致出现问题

#解决办法就是在执行一段代码(这里指修改balance的语句)时候只允许一个线程操作，其余线程必须等到该线程执行完才能执行
#如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，
#该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。
#由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。
#创建一个锁就是通过threading.Lock()来实现
def change_it(n):
    global balance
    #对余额一加一减
    balance = balance + n
    balance = balance - n

lock = threading.Lock()

def run_thread(n):
    for i in range(1000000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:不然相当于始终拿着锁的钥匙，却不用，这样就会形成阻塞，别的线程也被卡在这里
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


'''
锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，
首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，
导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止
'''