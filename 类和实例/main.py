
#class 类名(继承的父类)
class Student(object):
  def __init__(self,n,s):  #__init__是构造函数，其第一参数必须是self,表示创建的示例本身,相当于C++里的this指针
   self.name=n
   self.score=s
  def printObj(self):      #类中函数第一个参数必须是代表实例本身，不一定非要命名为self，其他符合命名规则的都可以
   print("%s---%s" % (self.name,self.score))#像上面__init__函数中将self全部换成std都是可以的
                                        #但是我们一般定义成slef就行
  def getGrade(self):
   if self.score>90:
    return "A"
   elif self.score<80 and self.score>60:
    return "B"
   else :
    return "C"

#类有了__init__函数，那么构造示例调用__init__函数就必须符合其参数(不需要考虑self参数)
#Python解释器自己会把实例变量传进去
s1=Student("QZQ",100)
print(s1)

#不像C++一样定义类的时候就必须将其属性全部定义
#python可以类的定义之后自定义其属性
s1.nickname="QZQ2514"
print(s1.nickname)
s1.printObj()
print(s1.getGrade())
#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
#并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，
#你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数

#不同于静态语言，例如C++中类的属性在类定义就规定好了，但是python，除了__init__中规定的属性，
#其余属性都是在实例化时候自己赋值的，像这里，s2增加了nicheng属性，但是s1就不存在nicheng属性
s2=Student("Jack",87)
s2.nicheng="xiaoqi"
print(s2.nicheng)
#print(s1.nicheng)