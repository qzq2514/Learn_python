import logging

#Python内置的logging模块可以非常容易地记录错误信息
def foo(s):
 print("foo函数开始")
 r=10/int(s)
 print("foo函数赋值结束")
 return r
def bar(s):
 print("bar函数开始")
 r=foo(s)*2
 print("bar函数赋值结束")
 return r
def main():
 try:
  print("try块开始:")
  r=bar('0')
 except Exception as e:
  print("Exception捕捉到:",e)
  logging.exception(e)
  
main()
print('END')