#打开的文件路径:当前路径默认是你启动程序的目录,比如这里我用Notepad++就是E:\Notepad++
#如果不知道启动程序的默认路径，可以使用一下方式获得
import os
print(os.getcwd()) 
print("--------------------")


#注意文件路径，不能简单写成D:\我的编程.....因为\是转义符号，必须写成"\\"或者用"/"代替"\\"
#再或者字符串前加"r"，像下面一样

#后面一个参数-标示符'r'表示读，这样，我们就成功地打开了一个文件
dear=open(r'D:\我的编程\newCode\python\文件读写\Dear.txt','r')


#文件不存在，则抛出IOError异常,存在则可以使用read函数获得文件内容
print(dear.read())

#close函数关闭文件，注意打开一个文件用完后一定记得关闭，不然占用操作系统的资源
#而且同一时刻，操作系统能打开的文件也是有限的
dear.close()


'''
由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，
为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现
'''
try:
 d1=open(r'D:\我的编程\newCode\python\文件读写\Dear.txt','r')
 print(d1.read())
finally:
 if d1:
  d1.close()
  
#这么写太复杂，可以用简单的with语句,不需要我们显式写出try,finally也能起到相同的效果
#而且会自动帮助我们调用close方法关闭文件
with open(r'D:\我的编程\newCode\python\文件读写\Dear.txt','r') as d2:
 print(d2.read())
 

print("-------------------") 
#文件太大，read()函数将内容全部读出来不太合适,可以采用read(size)读取指定大小的内容:
with open(r'D:\我的编程\newCode\python\文件读写\DearBig.txt','r') as db1:
 print(db1.read(10))   #参数表示读取指定大小的字符数
 

print("-------------------")  
##readline()函数读一行
with open(r'D:\我的编程\newCode\python\文件读写\DearBig.txt','r') as db2:
 print(db2.readline())   

 
print("-------------------")  
##readlines()函数将文章全部读出来封装成list，每一行是一个元素
with open(r'D:\我的编程\newCode\python\文件读写\DearBig.txt','r') as db3:
 ind=0
 for line in db3.readlines():
  print("%d:%s"%(ind,line))
  ind+=1