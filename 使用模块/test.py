import hello


#通过import hello导入hello模块
#这时必须执行hello.test()显示调用test函数.其实就像import math ,你不显式调用math.sqrt(9)，其不会自己调用的
hello.test()


'''
myName="QZQ2514"
__pubVar__="pubVar"
_priVar1="_priVar1"
priVar2__="priVar2__"
'''


#类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，
#__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名
print(hello.__name__) 
          
#正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等
print(hello.myName)

#类似_xxx和__xxx这样的函数或变量就是非公开的（protected和private），不应该被直接引用，比如_abc，__abc等
#我们这里直接模块里(像hello)定义的_xxx和__xxx所谓的非公开，并不是说就不能调用，并不是像C++类中的那种保护，
#私有变量那样严格的规定，所以看到这里，直接调用_xxx和__xxx也是没问题的
print(hello.__pubVar__)
print(hello._priVar1)
print(hello.priVar2__)