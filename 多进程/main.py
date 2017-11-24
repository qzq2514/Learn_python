from multiprocessing import Process
import os


#Unix/Linux系统中，使用os.fork()来创建当前进程的子进程,
#而在Windos系统中，使用multiprocessing模块下的Process构造函数来创建
#Process有两个参数,target是个函数，表示进程调用start()方法时，会运行target指定函数内的内容
#args表示子进程的一些信息，名字之类，作为target指定函数的参数，
def run_proc(name):
 print("运行子进程 %s (%s)"%(name,os.getpid()))
 
if __name__=="__main__":
 print("父进程 %s." % os.getpid())
 p=Process(target=run_proc,args=('test_qzq',))
 print("子进程即将运行!")
 p.start()                       #这里会调用run_proc方法
 p.join()                        #join方法表示运行完该子进程后，再继续运行，多用于进程的同步
 print("子进程运行结束!")
 
print("----------------------")

from multiprocessing import Pool
import time,random

#一下创建大量的子进程，可以使用进程池(Pool)对象
def long_time_task(name):
 print("运行任务:%s(%s)..." % (name,os.getpid()))
 start=time.time()
 time.sleep(random.random()*3)
 end=time.time()
 print("任务:%s 运行了 %0.2f seconds" % (name,(end-start)))

if __name__=="__main__":
 print("父进程:%s" % os.getpid())
 p=Pool(4)
 for i in range(5):
  p.apply_async(long_time_task,args=(i,))
 print("等待所有的子进程运行结束.........")
 p.close()          #进程池对象的close方法必须在jion方法之前，close方法表示不能再添加子进程了
 p.join()           #和之前一样，调用join表示等待进程池中所有子进程运行结束再继续运行程序
 print("所有的子进程运行已结束！")

 
 
 
'''
这里注意，任务0,1,2,3是立刻运行的,任务4必须等待之前4个子进程运行结束再运行
因为我们定义Pool对象的时候默认进程池大小为4，同时最多只能运行4个子进程,所以必须等待前4个子进程
运行结束再运行第5个
!!!由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果
'''