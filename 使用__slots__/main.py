
#动态绑定:
class Student(object):
 pass
 
s1=Student()
#python作为动态语言，其好处之一就是可以动态绑定属性和方法
s1.name="qzq2514"
print(s1.name)

def setAge(self,age):
 self.age=age
 
from types import MethodType
s1.set_Age=MethodType(setAge,s1)   
s1.set_Age(21)
print(s1.age)

s2=Student()
#print(s2.name)   #单独对实例动态绑定方法和属性，则对另一个实例是不可行的
#s2.set_Age(23)

#还可以直接对类动态绑定属性,这时相当于增加了类属性，也就是静态属性,并不影响已经绑定的同名实例属性
Student.name="QZQ"
print(s1.name)
print(Student.name)

#对没有该属性的实例，可以强制调用同名的类属性，这和前面说的类属性和实例属性是相吻合的
print(s2.name)


#我们可以通过添加类方法的办法，来给每个实例增加方法
def setAddress(self,addr):
 self.addr=addr

Student.set_Address=setAddress  #注意，这里通过class绑定方法，可以直接"类名".方法名=函数名,
                                #而像上面单独给实例添加方法，就必须使用MethodType函数

#给class绑定方法后，所有实例均可调用
s1.set_Address(43)
s2.set_Address(54)
print(s1.addr)
print(s2.addr)

#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的
#过程中动态给class加上功能，这在静态语言中很难实现








print("------------------")
#使用__slots__:
#我们可以使用__slots__限制类的动态绑定属性:
class People(object):
 __slots__ = ('name', 'age')        #使用tuple存放限定绑定的属性名

p1=People()
p1.name="qzq2514"
print( p1.name)
p1.age="21"
print( p1.age)
#p1.addr="XuZhou"         #People限定绑定的属性名只有'name'和'age',这里动态绑定addr属性，肯定错误"
#print( p1.addr)          #试图绑定addr属性将得到AttributeError的错误

class Man(People):
 pass
 
m1=Man()
m1.name="man2514"
print( m1.name)
m1.age="20"
print( m1.age)

#父类的slots限制对子类是没用的,子类可以使用任意的动态绑定属性
m1.addr="XuZhou"        
print( m1.addr) 
m1.nickname="XiaoQi"        
print( m1.nickname)




class Woman(People):
 __slots__=("addr")
 
w1=Woman()
 
w1.name="woman2514"
print( w1.name)
w1.age="20"
print( w1.age)

#如果子类也有__slots__属性，那么子类的实例可以动态绑定的属性名是"父类slots"+"子类slots"
w1.addr="SuiNing"        
print( w1.addr) 
#w1.nickname="XiaoQi"        
#print( w1.nickname)


#__slots__总结:
#1.父类有solts,子类没有solts，那么子类动态绑定属性为任意
#2.父类有solts,子类有solts，那么子类动态绑定属性为"父类slots"+"子类slots"
#(其实子类没有solts就可以看成任意属性，然后第一种就可以看成第二种的特例:"父类slots"+任意属性名=任意属性名)