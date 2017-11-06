#from 文件名 import 类名或函数名
from myHello import Hello


#type():
h=Hello();
h.hello()

print(type(h))       #h是Hello实例，<class 'myHello.Hello'>
print(type(Hello))   #Hello属于我们自定义的类型，它的类型就是type,<class 'type'>



print("-------------")
#python作为动态语言，其类的创建也是动态的,不仅可以通过class Hello(object):的方式创建，还可以通过type()
def fn(self,name="qzq2514"):
 print("fn Hello:%s"%name)

DyHello=type("DyHello",(object,),dict(sayHello=fn))
hh=DyHello()
hh.sayHello()
'''
要创建一个class对象，type()函数依次传入3个参数：
1.class的名称；
2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法:(object,)
3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上,fn函数第一个参数必须是self
'''
print(type(hh))       
print(type(DyHello))

'''通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
仅仅是扫描一下class定义的语法，然后调用type()函数创建出class

正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，
也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，
必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂'''