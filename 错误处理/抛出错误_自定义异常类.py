class myException(ValueError):
 pass

 
def foo(s):
  r=10/int(s)
  if(r==2):
   raise myException("foo函数得到2，异常结果")
  return r

#foo('5')     #抛出自己定义的异常,最后跟踪到我们自己定义的错误
 
 
 
print("------------------")
def foo2(s):
  r=10/int(s)
  if(r==2):
   raise myException("foo2函数得到2，异常结果")
  return r
  
  
def main():
 try:
  foo2('5')
 except myException as e:
  print("main函数捕捉到自定义的异常------")
  raise 
  
#main()


'''
这里我们在main中捕捉到异常myException后，打印了自己的一句话"main函数捕捉到自定义的异常"后又
raise,这样，会继续向上抛出异常，因为在main中捕捉到myException后打印那句话，仅仅是记录一下，
起不到错误跟踪的作用,而后面不带参数的raise,就会把当前错误原样抛出,也就说把myException又继续向上抛
这样，解释器会像之前一样一步一步跟踪定位，最终找到raise myException("foo2函数得到2，异常结果")
然后再打印"foo2函数得到2，异常结果"
'''


'''
也就说必须raise,不断将异常向上抛出，或者像记录错误.py中采用logging.exception(e)
这样才会将错误的出现路径一步一步定位,不然的话，仅仅就是在except异常块打印一下就没了
'''

print(">>>>>>>>>>>>>>>>>>>>>")
'''
此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型:
像下面，不仅会抛出ZeroDivisionError，还会抛出一个我们强制raise的ValueError
'''
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('强制raise的ValueError异常')