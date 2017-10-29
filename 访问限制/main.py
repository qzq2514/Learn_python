class Student(object):
  def __init__(self,n,s):  
   self.__name=n            #__属性名:定义私有属性,private,像C++一样，类内部函数可以直接访问，外界不能直接访问
   self.__score=s
   self._age=21             #一个下划线开头的实例变量名,比如这里 _age这样的实例变量外部是可以访问的，
                            #但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，
                            #但是，请把我视为私有变量，不要随意访问”
  def printObj(self):      
   print("%s---%s" % (self.__name,self.__score))
  def getName(self):
   return self.__name
  def getScore(self):
   return self.__score
  def setName(self,newName):
   self.__name = newName
  def setScore(self,newScore):
   self.__score=newScore
s1=Student("qzq2514",98)
s1.printObj() 
#外界不可以直接访问私有属性   
#print(s1.__name)

#只能通过函数的属性来访问或者修改类的私有属性,就类似javabean的set,get方法
print(s1.getName())
s1.setScore(79)
#不同于原来直接修改公开变量:s1.score="xxx",通过setScore函数可以对传入的参数进行一些判断，避免传入无效的参数
#比如说原来直接s1.score=-87也是可以的，但是明显是不对的，分数怎么可能有负数，在setScore函数中就可以对负数分数进行判断
print(s1.getScore())


'''
变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名
'''

'''
双下划线开头的实例变量通过某种强制转化也可以直接外部访问,原本不能直接访问__name是因为Python解释器对外把
__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉[哈哈，看到这里笑喷]
总之，既然原来规定了私有，就不要想方设法取直接外部访问
'''
print(s1._Student__name)


#注意下面这个有意思的事，原本__name属性时在类中私有的，我们没有强制得到，直接进行赋值：s1.__name="hahahah"
#竟然是可以的，但是我们我们通过getName()得到姓名，竟然还是"qzq2514",并不我们预想的"hahahah"
#表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
#内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量
print(s1.getName())
#print(s1.__name())
s1.__name="hahahah"
print(s1.getName())
print(s1.__name)
