class Student(object):
#像c++,java一样，python也可以定义类属性，就类似于静态属性
 name="ClassName"
 def __init__(self,name):
  self.name=name


s1=Student("qzq")
#当实例有自己的属性，我们用实例名调用的话是实例自己的属性
print(s1.name)
#可以直接使用类名来调用类属性
print(Student.name)

#当我们删除了实例的属性，可以用实例调用同名的类属性
del s1.name
print(s1.name)
#这里s1.name="hahahah"相当于又给实例增加了实例属性，改变的其不会影响类属性
s1.name="hahahah"
print(s1.name)
print(Student.name)
 
 
#类属性就类似于类的静态属性，是属于类的实例所共有的