
print("assert----------------------")
#assert(断言):
#当我们调试程序时，需要看到变量的值到底是什么，如果直接使用print打印出来，在调试结束后再一一删除，未免
#复杂，不删除的话，又会打印一系列垃圾信息,这时我们就需要用到assert-断言
def foo(s):
 r=int(s)
 assert r!=0,"出现除数零"    #这句话的意思的是"我断言r!=0,不然就打印'出现除数零'这句话"
 return 10/r

#如果断言失败，assert语句本身就会抛出AssertionError
#foo(0)

#程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert
#例如:python3 -O main.py
#关闭后，你可以把所有的assert语句当成pass来看




print("logging----------------------")
#logging:
import logging
logging.basicConfig(level=logging.INFO)  #这句话千万不能忘了，不然logging.info的信息不会打印

s='0'
r=int(s)
logging.info("计算得r=%s"%r)
print("10/r",10/r)

'''
这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息(没看懂!!!)
'''





print("pdb----------------------")
#pdb:
'''
启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态,例如: python3 -m pdb err.py
1.命令l来查看代码
2.命令n可以单步执行代码
3.命令p 变量名来查看变量
4.命令q结束调试，退出程序
'''

#pdb.set_trace():
'''升级版的pdb，不必须一行一行代码的进行运行调试
相当于断点，程序会自动运行到我们设置的断点处,设置断点:pdb.set_trace()
1.命令p查看变量
2.命令c继续运行
'''
