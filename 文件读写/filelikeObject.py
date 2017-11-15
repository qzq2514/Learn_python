#像main.py中介绍的一般的读取文本文件的对象有个read方法，其实除了文件，还可以进行字节流,网络流，自定义流的读取
#这在Python中统称为file-like Object



#用'rb'模式读取视频图片
with open(r'D:\我的编程\newCode\python\文件读写\temp.jpg','rb') as t1:
 print(t1.read())  #输出一连串十六进制
 

 
print("-------------")
#添加encoding='xxx'读取指定编码的文件,对于编码不规范的文件，可能会出现UnicodeDecodeError
#errors='xxx'是遇到这种未知编码方式的字符的处理方式，最简单的就是忽略
t2=open(r'D:\我的编程\newCode\python\文件读写\Dear.txt','r',encoding='gbk', errors='ignore') 
print(t2.read())






#写文件同样适用open函数，不同的是使用'w'模式写一般文本文件,'wb'写二进制文件
w1=open(r'D:\我的编程\newCode\python\文件读写\DearW.txt','w')
#使用write哈数不断写入内容，添加在文件末尾
w1.write("我是自写的文件的内容!!\n")
w1.write("我是第二行。")

#像java一样，write只是相当于将内容写到缓存区，必须flush或者关闭文件，才能真正将内容写到文件中
#所以我们必须手动关闭文件,或者直接用with语句，让解释器帮我们关闭
w1.close()



#要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码,像之前读一样
#我们就用encoding='xxx'参数就行