
#__getattr__
class student1(object):
 def __init__(self):
  self.name="QZQ2514"
  

s=student1()
print(s.name)
#print(s.score)没有赋值，直接调用实例的属性,会报错

class student2(object):
 def __init__(self):
  self.name="qzq2514"
 def __getattr__(self,attr):
  if attr=="score":
   return 99
  elif attr=="name":
   print("调用name属性")
  elif attr=="getName":
   return lambda :"姓名:"+self.name
  raise AttributeError("\'student2\' object has no attribute:",attr)
   
s=student2()
print(s.name)
print(s.score)        #调用不存在，即未赋值的属性，则会调用__getattr__(self,不存在的属性名)
                      #但是要注意，调用存在的属性，像name属性，就直接调用，不会调用__getattr__方法
print(s.getName())    #调用不存在的方法，也会调用__getattr__,但是这里稍微不同的是调用方法要加括号
#print(s.address)      #调用的方法不仅不存在，而且在__getattr__中也没有判断处理，那么就返回None，
                      #因为__getattr__默认返回的就是None,除非这里你在__getattr__中做了处理，
                      #只对指定的不存在的属性进行处理，其余抛出异常，像这里的raise AttributeError
                      
                      
                      
#应用:简单API链式调用:
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        #print("path",path)
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
    
    
cha=Chain()
print(cha.status.user.timeline.list) #打印'/status/user/timeline/list'
#cha是Chain的实例，cha._path=""调用不存在的status属性，进而转到__getattr__(self,status),返回Chain("/status")
#然后又调用user属性，调用__getattr__(self,user),返回Chain("/status/user")，不断调用，直到返回
#Chain("/status/user/timeline/list"),直接打印这个对象，调用__str__方法，就打印出了其_path属性


#github复杂链式调用
class ChainGit(object):
    def __init__(self, path=''):
        self._path = path
    def users(self,name):
     return Chain('GET /users/%s' % name)
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
    
cg=ChainGit();
print(cg.users('michael').repos)      #变成一般的github的网址形式:GET /users/michael/repos








#__call__:
class student3(object):
 def __init__(self,name):
  self.name=name
 def __call__(self):
  print("student3:",self.name)
  
ss=student3("qzq2514")
#__call__方法允许我们直接向调用函数一样调用对象,像下面的ss(),注意不能加参数
ss()

#通过callable函数来判断变量能不能被调用
print(callable(ss))
print(callable(max))  #判断max函数
print(callable([1,2,3]))#判断list
 