class Animal(object):
 def run(self):
  print("Animal is running!")

#括号里是继承的父类的类名
class Dog(Animal):
 def run(self):
  print("Dog is running!")
 def eat(self):
 #子类可以定义自己的函数
  print("Dog is eating!")

class Cat(Animal):
#子类可以定义和父类同名的方法名，实现覆盖
 def run(self):
  print("Cat is running!")
d1=Dog()

#子类拥有父类的属性和方法,可以直接调用
d1.run()
#子类也可以直接调用自己的特有方法
d1.eat()


c1=Cat()
c1.run()

#我们自己定义的类和python自带的类型没啥区别，我们同样可以使用isinstance来判断变量是不是某各类的实例
print(isinstance(c1,Cat))      #True
print(isinstance(c1,Dog))      #False
#在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。(但是，反过来就不行)
print(isinstance(c1,Animal))   #True


#多态：
def run_twice(animal):
 animal.run()
 animal.run()


run_twice(Animal())      #打印两遍Animal is running!
run_twice(Dog())         #打印两遍Dog is running!
run_twice(Cat())         #打印两遍Cat is running!

'''
多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
因为Dog、Cat……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，
因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思


对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，
而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，
这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，
只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
1.对扩展开放：允许新增Animal子类；
2.对修改封闭：不需要修改依赖Animal类型的run_twice()等函数
'''

class People(object):
 def run(self):
  print("People is eating!")
  
#不像静态语言(例如Java),当函数参数是Animal类型的，那么传入的参数实例必须是Animal或者其子类的
#但是对于像python这样的静态语言，则不一定需要传入Animal类型。
#像这里我们只需要保证传入的对象有一个run()方法就可以了
#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
#一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
p1=People()
run_twice(p1)