
#metaclass
#除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
#metaclass(元类)类似于C++中的虚类，是类的模板，类是元类的实例


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
 def __new__(cls,name,bases,attrs):
  attrs["myAdd"]=lambda self,value:self.append(value) #自定义myAdd方法，类似于append方法,使用lambda(函数)赋值
  return type.__new__(cls,name,bases,attrs)
  
  
'''
__new__()方法接收到的参数依次是：

1.当前准备创建的类的对象；
2.类的名字；
3.类继承的父类集合；
4.类的方法集合。
'''
class myList1(list,metaclass=ListMetaclass):
 pass

l1=myList1()
l1.myAdd("qzq2514")
print("myList1",l1)

ll=list()
#ll.myAdd("qzq2514")     #普通的list没有我们定义的myAdd方法
print(ll)


#有人会感觉，这样在metaclass中添加我们自己方法有啥意义，直接在myList1中我们添加自定义方法不是更简答，
#就像下面myList2我们在myList2中自定义一个添加方法addAnother
class myList2(list,metaclass=ListMetaclass):
 def addAnother(self,value):
  self.append(value)
  
l2=myList2()
l2.addAnother("qzq2514")
print("myList2",l2)

#这样也是可以达到自定义类和拓展方法的效果的，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子
#将在ORMFramework.py中进行展示