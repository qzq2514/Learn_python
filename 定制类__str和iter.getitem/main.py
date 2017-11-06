
#__len__  ;  __str__
class Student(object):
 def __init__(self,n):
   self.name=n
 def __len__(self):
   return len(self.name)
 def __str__(self):
   return "学生:"+self.name
 #在交互界面直接敲变量不用print，打印出来的实例还是<__main__.Student object at 0x109afb310>形式
 #这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
 #而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
 #解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法
 __repr__ = __str__
 
 
 
 
 
#像之前给类添加__len__方法，我们就可以直接将Student类的实例作为len函数的参数进行调用
#这就是使用函数来装饰类
s1=Student("qzq2514")
print(len(s1))   

#使用__str__装饰，类似java中的toString方法，可以按照我们的方式打印出实例
print(s1)         
 
 
print("----------------")
#__iter__   ;   __next__
'''
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法
拿到循环的下一个值，直到遇到StopIteration错误时退出循环
'''
class Fib(object):
 def __init__(self,maxV):
  self.f1,self.f2=0,1
  self.max=maxV
 def __iter__(self):
  return self
 def __next__(self):
  self.f1,self.f2=self.f2,self.f1+self.f2
  if self.f1>self.max:
   raise StopIteration()
  return self.f1
  
for x in Fib(200):  #打印小于200的斐波那契数列
 print(x)
 

 

print("----------------")
#__getitem__
#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素
#print(Fib(100)[5])   利用下标访问会出错

class FibIndex(object):
 def __getitem__(self,n):     #n代表下标，从0开始
  a,b=1,1
  for x in range(n):
   a,b=b,a+b
  return a

#实现了__getitem方法后就可以用下标访问元素
print(FibIndex()[1])

#我们使用像在list中用到的切片来对FibIndex取值，但是这里会报错，因为我们这里的__getitem__方法
#只考虑了下标整数的情形，没考虑切片情况
#print(FibIndex()[1:5])     #FibIndex不可以使用切片

#下面定义可以使用整数下标和切片的情况
class FibIndexWithSlice(object):
 def __getitem__(self,n):     
  if isinstance(n,int):       #下标是整数
   a,b=1,1
   for x in range(n):
    a,b=b,a+b
   return a
  if isinstance(n,slice):     #下标是切片
   start=n.start          #获得切片的起始和结束位置
   stop=n.stop
   if start is None:          #没有起始下标，则从下标0开始
    start=0
   a,b=1,1
   reslist=[]
   for x in range(stop):
    if x>=start:
     reslist.append(a)
    a,b=b,a+b
   return reslist

#在__getitem__方法中对切片情况进行判断后，就可以对自定义的类使用切片
print(FibIndexWithSlice()[5])
print(FibIndexWithSlice()[2:5])
print(FibIndexWithSlice()[:5])
print(FibIndexWithSlice()[:5:2])    #但是这里我们并没有考虑step的情况，所以这里带有步长的切片并不会起到效果
                                    #可是不会报错的，顶多我们就不步长，我们在__getitem__函数中for循环默认步长为1
                                    
'''
也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，
用于删除某个元素。总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，
这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口
'''