
#1.type():
#我们可以使用type函数来获得变量对象的类型
#不仅仅可以返回int,str类型,还可以返回类的类型和函数的类型
print(type(123))
print(type("wer"))

class Animal(object):
 pass
print(type(Animal()))
print(type(abs))

print(type(123)==type(234))
print(type("hehe")==type(234))  #可以使用type对两个变量的类型进行相同性判断
print(type("hehe")==str)
print(type(989)==int)           #可以直接使用int,str来进行判断


import types
def myfun():
 pass
print(type(myfun)==types.FunctionType)    #判断自定义函数
print(type(abs)==types.BuiltinFunctionType) #判断python内置函数
print(type(lambda x:x**2)==types.LambdaType) #判断　lamdba 表达式
print(type((x**2 for x in range(10)))==types.GeneratorType)  #判断生成器


#2.isinstance():
#能用type()判断的基本类型也可以用isinstance()判断：
print(isinstance(12,int))
print(isinstance(b'a', bytes))

#还可以使用isinstance来判断一个变量是不是多个类型中的其中一种
print(isinstance(12,(int,str,float,list)))

#3.dir():
#使用dir函数打印某类型的所有属性和方法
#比如dir(str)它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
#print(dir(str))

#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
#在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
#它自动去调用该对象的__len__()方法，所以，下面的代码是等价的:
print(len("ABC"))
print("ABC".__len__())
print("ABC".lower())


#对于自定义的类，想要同样能使用len()函数，就要在类中实现__len__方法
class myDog(object):
 def __init__(self,x):
  self.x=x
 def __len__(self):
  return 123
 def power(self):
  return self.x*self.x
 

#print(dir(myDog))  #自定义类的默认的方法有很多，包括__len__，__class__等等
d1=myDog(23)
print(len(d1))
d1.y=90
print(hasattr(d1,'x'))  #可以使用hasattr判断实例有没有某种属性
print(hasattr(d1,'y'))  #当然也可以判断类定义之外的实例的属性

setattr(d1, 'y', 9999)          #可以使用setattr对实例进行属性的赋值
setattr(d1, 'name', "qzq2514")  #setattr还可以创建新舒属性并同时赋值
print(getattr(d1,'name'))       #不仅可以像之前一样用点获得属性，还可以用getattr获得实例的属性
print(d1.y)

#print(getattr(d1,'z'))           #如果试图获取不存在的属性，会抛出AttributeError的错误
print(getattr(d1,'z',9090))       #可以传入一个default参数，如果属性不存在，就返回默认值


print(hasattr(d1,"power"))       #还可以使用hasattr来判断实例有没有某种方法
print(getattr(d1,"power"))
fn=getattr(d1,"power")            #甚至可以接收getattr返回值
print(fn())                        #之后调用fn()和调用d1.power()一样