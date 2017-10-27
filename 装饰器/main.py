import functools

#函数也是一个对象，函数可以被赋值给变量，并且通过变量来调用该函数
def now():
 print("2017-10-27")
 
f=now

#这里通过now()调用和f()调用原now函数效果是一样的
now()
f()

#函数对象有个__name__属性，可以得到函数的名字
print(now.__name__)
print(f.__name__)

#现在我们想要增加now函数的功能，但是又不希望改变now函数的定义，也就是说在now函数之外如果能有什么在now
#函数调用时自动调用就好了，python确实有这样一个特性-"装饰器"

def log(func):
 def wrapper(*args,**kw):
  print("Call %s:" % func.__name__)
  return func (*args,**kw)
 return wrapper
 
#观察上面的log就是一个装饰器-"decorator",接收一个函数作为参数，并返回一个函数
#我们要借助Python的@语法，把decorator置于函数的定义处
@log
def now():
    print('2015-3-25')

now()
#现在我们调用now函数,不仅会执行now函数中的内容，还会在now()函数之前打印: Call now:
#其实我们通过把装饰器@log放在now函数定义前，相当于执行了:   now = log(now),也就是相当于now=wrapper
#来理一下思路:
#@log放在now函数定义前,我们now = log(now),也就是now=wrapper
#然后我们调用now(),就是相当于调用wrapper函数，而我们注意log函数中定义的wrapper,先是打印"Call [函数名]"
#然后返回的时候调用func(*args,**kw),注意，这里*args,**kw表示可以接受任何参数，
#所以now()发生了两个事情，先是打印"Call [函数名]",之后调用自身原本只是打印时间的now()

#我们这时候打印now.__name__可以看到，now.__name__=wrapper
print(now.__name__)


#如果decorator本身有参数，那么定义就比较复杂:
def log(text):
    def myDecorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            func(*args, **kw)
            return None
        return wrapper
    return myDecorator

@log("现在执行")
def now():
    print('2015-3-25')

now()

#再来理一下这个三层嵌套的decorator,在now之前写上@long("现在执行")，相当于执行了:
#now = log('execute')(now)
#我们来剖析下上面的句子,先是执行log('execute'),然后返回myDecorator函数,之后再调用返回的myDecorator函数,
#并将now作为参数，也就是now=myDecorator(now),之后就和上面两层的decorator一样了
#注意这里有个小细节，就是在wrapper函数中，我不同于上面的wrapper,而是执行一次打印"现在执行 [函数名]:"
#后直接调用func函数，也就是原now函数，这样相比于原来直接返回return func (*args,**kw),更有助于帮助我们了解其中的
#执行步骤，但是两者的效果其实是一样的

#现在我们打印now.__name__,可以看到同样now.__name__=wrapper,
print(now.__name__)

#因为返回的那个wrapper()函数名字就是'wrapper'，
#所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错

#我们可以通过Python内置的functools.wraps进行函数属性的复制，比如在两层的decorator中:

def log(func):
    @functools.wraps(func)           #将func函数的属性赋值给下一行定义的wrapper函数
    def wrapper(*args, **kw):        #注意，这里使用@functools.wraps函数需要import functools
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
 
@log
def now():
    print('2015-3-25')
    
print(now.__name__)

#对于三层的decorator，同样也是在def wrapper(*args, **kw):上一行加上@functools.wraps(func),就不做演示



#练习1:编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
print("-------------")
def AllPrint(func):
 def wrapper(*args,**kw):
  print("begin call")
  func(*args,**kw)
  print("begin call")
  return None
 return wrapper

@AllPrint
def testAllPrint():
 print("我是testAllPrint()")
 
testAllPrint()

'''练习2:写出一个@log的decorator，使它既支持
@log
def f():
    pass
又支持：
@log('execute')
def f():
    pass
'''
print("-------------")
def logs(text):
    if type(text) == type('ss'):      #先判断参数,下面直接分两种情况进行两层或者三层嵌套
        def decorator(func):
            @functools.wraps(func)
            def wrappers(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrappers
        return decorator
    else:
        def wrappers(*args, **kw):
            print('call %s():' % text.__name__)
            return text(*args, **kw)
        return wrappers
        
        
@logs
def now():
    print('2015-3-25')
    
now()

@logs("现在开始调用")
def now():
    print('2015-3-25')
    
now()