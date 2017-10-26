

def lazy_calcu(*args):
 def calcu():
  res=0
  for x in args:
   res+=x;
  return res
 return calcu
 
#高阶函数不仅可以将函数作为参数，同时还可以将函数作为返回值
#这里lazy_calcu将其内部定义的calcu函数返回，相当于f=calcu
#只有当调用f()时候，才会真正将和求出来
f=lazy_calcu(1,2,3,4,5)
print(f)
print(f())


#像上面内部函数calcu可以引用外部函数lazy_calcu的参数和局部变量
#当lazy_calcu返回函数calcu时，相关参数和变量都保存在返回的函数calcu中，这种称为“闭包（Closure）”
#lazy_calcu(1,2,3,4,5)

#这里要注意的一个小细节，就是返回函数的外层函数每次都会返回新的函数
#即便传入的是相同的参数，也是返回新的函数
ff=lazy_calcu(1,2,3,4,5)
print(f==ff)

#f()和ff()的调用结果互不影响



#闭包问题:

def count():
 funcs=[]
 for i in range(4):
  def func():
   return i
  funcs.append(func)
 return funcs

resFunc=count();
print(resFunc)
f1=resFunc[0]
f2=resFunc[1]
f3=resFunc[2]

print("f1():",f1())
print("f2():",f2())
print("f3():",f3())

#这里我们可以看到一个问题，那么这里count函数中的for产生三个函数，并存放在count返回的集合中
#按理说我们期待的是f1,f2,f3调用后分别输出1,2,3，可是实际输出的是3,3,3
#这时因为这三个函数都引用了for循环中的i变量，并不是每次的for循环都当即调用f1或f2,f3函数
#等到3个函数都返回时，它们所引用的变量i已经变成3,这时三个函数都调用i并返回i,所以也就全部返回输出3

#所以牢记:返回函数不要引用任何循环变量，或者后续会发生变化的变量

#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
#无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))             # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
    
f1, f2, f3 = count()       #还可以这样接收是list类型的返回值

print("f1-",f1())
print("f2-",f2())
print("f3-",f3())

#拓展:测试返回list类型的返回值，并利用list中的元素直接赋值
def fun():
 ll=[]
 ll.append('1')
 ll.append('2')
 ll.append(999)
 return ll
 
a,b,c=fun()          
print(a)
print(b)
print(c)