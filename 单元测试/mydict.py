class Dict(dict):
 def __init__(self,**kw):
  super().__init__(**kw)
  
 #d.属性名会调用 __getattr__方法，key=属性名
 def __getattr__(self,key):
  print("调用__getattr__",key)
  try:
   return self[key]
  except KeyError:
   raise AttributeError(r"Dict没有属性:",key)

 def __setattr__(self,key,value):
  print("调用__setattr__",key)
  self[key]=value

  
  
  
  
d = Dict()
#value=d["empty"]     #不会调用__getattr__
#value = d.empty     #会调用__getattr__