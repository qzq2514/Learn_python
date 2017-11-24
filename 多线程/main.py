import time,threading

'''
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，
对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块
'''
def loop():
 print("线程:%s正在运行....." % threading.current_thread().name)
 n=0
 while n<5:
  n=n+1
  print("线程:%s正在运行第%s次" % (threading.current_thread().name,n))
  time.sleep(1)
 print("线程:%s运行结束....." % threading.current_thread().name)
 
print("main中当前运行线程是:%s....." % threading.current_thread().name)
#运行py文件,默认的线程是主线程:MainThread,Python的threading模块有个current_thread()函数，可以随时返回当前程序运行
#的线程的名称,子线程在创建的时候可以自己指定，其仅仅其标识作用
#名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
t=threading.Thread(target=loop,name="Loop_Thread") #和进程一样，Thread线程构造函数传入target参数
t.start()
t.join()          
print("main中线程:%s运行结束....." % threading.current_thread().name)

print("-----------------")