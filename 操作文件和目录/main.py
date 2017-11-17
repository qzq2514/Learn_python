import os

#在python中也有一些函数方法可以像命令行的命令dir,cd,md之类的一样调用操作系统的接口
#对文件和目录进行操作

#os.name得到操作系统名字，
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.name)

#uname()函数可以获得操作系统相关的更详细的信息，但是在window系统上无效
#print(os.unname)


#environ得到环境变量
print(os.environ)

print("--------------------")
#获取某个环境变量的值，可以调用os.environ.get('key')
print(os.environ.get('path'))

print("--------------------")
#操作文件和目录的一些函数在os中，也有在os.path中

#获取当前目录的绝对路径
print(os.path.abspath("."))

#想在某个目录下面创建目录，先要把新目录的完整路径给表示出来
#然后mkdir函数正式创建目录
'''os.path.join(r'G:','myTest')
os.mkdir(r'G:\myTest')
print("--------创建目录成功!")
os.rmdir(r'G:\myTest')
print("--------删除目录成功!")'''

#将路径分割，最后一部分是文件名称(其实实质就是按照最后一个文件目录符分割)
l=os.path.split(r"\Users\michael\testdir\file.txt")
print(l)

#splitext将文件后缀名和其余部分分割(其实实质是从点.左右分割)
e=os.path.splitext(r"\Users\michael\testdir\file.txt")
print(e)
print(e[1])     #e[1]就是文件拓展名



#os.rename(r"G:\myTest\myfile.txt",r"G:\myTest\myfileCopy.py")
print("修改文件名成功!")


#使用python进行过滤，下面实现过滤得到指定文件夹下的所有文件夹
ll=[x for x in os.listdir(".") if os.path.isdir(x)]
print(ll)

lll=[x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1]==".dll"]
print(lll)





#小结:Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中