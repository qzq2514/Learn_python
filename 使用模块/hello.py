#!/usr/bin/env python3       #第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-      #第2行注释表示.py文件本身使用标准UTF-8编码      

' a test module '       #该是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
__author__ = 'Michael Liao' #使用__author__变量把作者写进去

#以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。

import sys
'''
导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。;
sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
运行python3 hello.py获得的sys.argv就是['hello.py']；
运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]
'''

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

'''
当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过
命令行运行时执行一些额外的代码，最常见的就是运行测试
'''
if __name__=='__main__':
    test()

#在不是命令行而是在文件中，这里if __name__=='__main__':判断的效果如下:
#如果是直接运行该hello.py文件，那么这里__name__会被赋值为'__main__',相当于该hello模块是主函数入口
#那就会执行if内的代码调用test函数
#相反，如果是在其他文件，例如该文件同级目录下的test.py中通过import hello导入hello模块
#那么hello模块的__name__就不是__main__
#这时必须执行hello.test()显示调用test函数.其实就像import math ,你不显式调用math.sqrt(9)，其不会自己调用的

#但是这里print("hahahah")是只要你import hello就会调用的，不同于test()
print("hahahah")


myName="QZQ2514"
__pubVar__="pubVar"
_priVar1="_priVar1"
priVar2__="priVar2__"