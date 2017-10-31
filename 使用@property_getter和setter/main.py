class student(object):
 def __init__(self,s):
  self.score=s
 
 def getScore(self):
  return self.score
  
 def setScore(self,value):
  if not isinstance(value,int):
   raise ValueError("分数必须为整数int")
  if value<0 or value>100 :
   raise ValueError("分数必须在0~100之间")
  self.score=value
  
s1=student(98)
#这里我们看到，如果我们直接 实例名.属性名进行赋值，那么会产生很多问题，像范围，数据类型等一系列问题
#但是头疼的是，都不会报错
s1.score=9090
print(s1.score)
s1.score="kiueir"
print(s1.score)

#为了解决上面的问题，我们使用get,set来对属性进行设置和读取
#我们在函数内进行属性的范围，类型等判断，这样可以避免上面出现的一些列问题
#s1.setScore(9090)             #范围错误
#s1.setScore("kiueir")         #数据类型错误


#但是实例名.方法名()的办法进行属性设置，又显得臃肿，我们想着，能不能我们就用一开始s1.score=9090,s1.score="kiueir"
#的形式进行属性赋值，但是出现范围，类型等错误的时候又会报错,感觉像是在做逼梦一样，可是梦想还是要有的，因为这个真的
#可以实现,我们重新定义student:
class student2(object):
 #def __init__(self,s):
  #self.score=s
 
 #使用@property来把原来的一个getter变成属性，可以直接得到
 @property
 def myScore(self):
  return self._score
  
 #使用@属性名.setter将一个setter方法变成属性赋值
 #注意这里属性名要和上面的@property装饰的函数名一致,表明这两个是一对
 #而这里@myScore.setter装饰的函数名score就是类似于属性名，下面可以直接实例名.score进行赋值
 #且@property标记的方法 必须 写在 @方法名.setter 之前。
 
 @myScore.setter
 def score(self,value):
  if not isinstance(value,int):
   raise ValueError("分数必须为整数int")
  if value<0 or value>100 :
   raise ValueError("分数必须在0~100之间")
  self._score=value                  #注意类中我们用的真实的属性名其实是_score带有下划线的
                                     #如果我们仍用score,那么这里变成self.score=value,就会不断递归
                                     #地调用score(self,value)函数，因为每次赋值都会调用   

  #还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
 @property
 def grade(self):
  if self._score>90:
   return "A"
  elif   self._score>75:
   return "B" 
  elif   self._score>60:
   return "C"
  else:
   return "D"
    
   

s2=student2()
#s2.score=900            #范围报错
#s2.score="kiueir"       #类型报错
s2.score=90              #我们调用score可以直接赋值，要知道，其实这里是调用score函数对_score进行赋值
print(s2.score)   
s2._score="9090"         #如果我们直接调用_score,那么就是一开始我们直接调用属性，不会对属性进行范围，而类型m等判断
print(s2._score) 

s2.score=89              
print(s2.score)          #有@property又有@myScore.setter的属性，获得时必须调用@myScore.setter下面的函数名，
                         #即这里必须s2.score,不能是s2.myScore
print(s2.grade)           #对于只读属性，即只有@property,获得时，直接调用@property下面的函数名，也就是这里的grade





#练习：请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
 
 @property
 def width(self):
  return self._width
  
 @property
 def height(self):
  return self._height
  
 @width.setter
 def width(self,value):
  self._width=value
  
 @height.setter
 def height(self,value):
  self._height=value
  
 @property
 def resolution(self):
  return self._height*self._width

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution


