import json

#dict对象可以直接被序列化为json的{},不过，更多时候，我们喜欢用class来表示对象
class student(object):
 def __init__(self,name,age,sex):
  self.name=name
  self.age=age
  self.sex=sex
  
s=student("qzq",21,"male")
#print(json.dumps(s))       #直接将对象序列化为json是不可以的




#前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，
#dumps()方法不知道如何将Student实例变为一个JSON的{}对象
#我们只需要为Student专门写一个转换函数，再把函数传进去即可
def student2dict(s):
 return{
   "myName":s.name,
   "myNge":s.age,
   "mySex":s.sex
 }

#这样就可以先将对象s最为参数传入student2dict函数，然后返回一个dict对象，然后再　进行json化
print(json.dumps(s,default=student2dict)) 




class teacher(object):
 def __init__(self,name,age,sex,salary):
  self.name=name
  self.age=age
  self.sex=sex
  self.salary=salary

#如果我们再定义一个teacher类,将其变为json再为其写一个teacher2dict函数未免太复杂
#我们可以使用对象的__dict__,返回的就是一个dict
t=teacher("Zhu",30,"female","6000")
print(json.dumps(t,default=lambda obj:obj.__dict__)) 



#先将student对象变为json以备用
js=json.dumps(s,default=student2dict)

print("js:",js)
#如果想要将json变为对象，同样需要定义一个函数,然后使用json.loads方法将字符串变为python对象
def dict2student(d):
 return student(d["myName"],d["myNge"],d["mySex"])

#使用json.loads将json字符串变为python对象
ss=json.loads(js, object_hook=dict2student)
print(ss)
print("name:",ss.name)






print("练习----------------")
#练习:对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
#输出中的name是'中国' 中的ascii 字符码，而不是真正的中文。
#这是因为json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False