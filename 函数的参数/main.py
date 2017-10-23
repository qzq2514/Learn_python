
#1.位置参数，固定了参数的个数和对应位置的参数类型
#传入的两个值按照位置顺序依次赋给参数x和n。
#两个参数的顺序必须一一对应，且少一个参数都不可以
def power1(x,n):
 res=1
 while n>0:
  n=n-1
  res=res*x
 return res

print(power1(5,3))
#print(power1(5))    #少参数，错误


#2.默认参数,对应位置没有参数传递的就使用默认参数值
#要求:(1).必选参数在前，默认参数在后，否则Python的解释器会报错,因为实参依次从头到尾赋值给形参
#     ()
def power2(x,n=2):
 res=1
 while n>0:
  n=n-1
  res=res*x
 return res

print(power2(5,3))    #完整参数的调用，这时候和power1没区别
print(power2(5))      #缺省参数的调用，这里使用默认的n=2，相当于power2(5,2)

def power3(x=9,n=3):
 res=1
 while n>0:
  n=n-1
  res=res*x
 return res

print(power3(2))      #对于含有多个默认参数，将实参一一从前向后赋值给参数，所以这里相当于power3(2,3)
print(power3(n=2))    #想跳过某个默认参数进行赋值，就要在调用该函数时显示地进行赋值，所以这里相当于power3(9,2)


def strAdd1(l=[]):         #这里的函数参数有个比较有意思的现象
 l.append('end')
 return l

print(strAdd1(['1','2','3']));  #只是简单的有参的函数调用，那么没有问题，就执行strAdd1函数内容在list后面添加'end'

print(strAdd1())        #但是有意思的是如果一直都是用默认参数调用strAdd1,那么打印出来后，会依次添加'end'
print(strAdd1())        #感觉像是函数每次都“记住了”上次添加了'END'后的list。
print(strAdd1())        #原因是在定义函数strAdd1时候，就产生了一个l函数，并真真实实指向了一块内存中的list变量区域[]
                        #之后每次以默认参数形式调用时，都会改变l的内容，不再是函数定义时的空list[]


def varAdd(n=2):        #所以定义参数的时候，默认参数必须指向不变对象，这里以varAdd函数的默认参数n指向不变的变量类型
 n+=1;                  #可以看到内次默认调用varAdd后，输出的都是3并没有依次添加n
 return n

print(varAdd())
print(varAdd())
print(varAdd())

def strAdd2(l=None):     #这里使得默认参数l指向不变的None,这样，即便之后每次无参默认形式调用，
 if l is None:           #也不会出现上面出现的问题         
  l=[]
 l.append('end')
 return l

print(strAdd2())
print(strAdd2())
print(strAdd2())




#3.可变参数:*元素封装在tuple中

#如果我们想求一系列数字的平方和但是不知道有多少个数，我们最容易想到的就是装载一个list中，然后遍历，如下:
def sqrtSum1(l):
 sum=0
 if isinstance(l,(list)):
  for x in l:
   sum+=x*x;
 return sum
 
print(sqrtSum1([1,2,3,4]));
print(sqrtSum1([1,2,3]));

def sqrtSum2(*l):         #和之前位置参数定义一个list或tuple参数相比，可变参数在参数前面加一个*即可
 sum=0                 
 for x in l:
  sum+=x*x;
 return sum
 
print(sqrtSum2(1,2,3,4)); #可变参数可以直接传入多个不定数量的参数,在函数中，就会将这0个或多个变量封装成一个tuple
print(sqrtSum2(1,2,3));
ll=(2,3,4,5)       
print(sqrtSum2(*ll));    #在list或者tuple变量名前加上*表明将list或者tuple中的元素当做可变参数传递到函数中


#4.关键字参数: **元素封装在dict中
#关键字参数在参数前面加两个*,即**,这是带有参数名的参数，会自动封装成一个dict,也就是字典集合
#关键字参数也可以传入不定数量的参数
def printPerson1(name,age,**kw):
 print("name:",name,"age:",age,"other:",kw)
 
printPerson1("QZQ",21,city="XuZhou",xian="SuiNing")
printPerson1("QZQ",22,city="XuZhou",xian="SuiNing",hobby="Read")
otherInfo={"city":"XuZhou","xian":"SuiNing","hobby":"Read"}
printPerson1("QZQ",23,**otherInfo) #和可变参数一样，也可以在dict类型的变量前加上**直接将其中元素编程关键字参数传递到函数中
                                  #需要注意的是，这里只是将otherInfo中的元素重新拷贝一份封装在kw中，在函数中
                                  #对kw的修改不会改变otherInfo
                        

#5.命名关键字参数
#关键字参数中我们可以传入不定的参数，如果我们要判断dict集合中有没有我们想要的关键字
#那么就需要我们自己在函数中进行判断，如下:
def printPerson2(name,age,**kw):
 if "city" in kw:
  print("有城市信息")
 if "xian" in kw:
  print("有县级信息")
 print("name:",name,"age:",age,"other:",kw)    
#关键字参数只是在函数内部进行判断，不影响我们的可变参数，我们仍然可以不受限制的传入不定量的参数
printPerson2("QZQ",22,city="XuZhou",hobby="Read")

#对于命名关键字，我们用单独的一个*进行分割，后面的变量名是必须传进去的
def printPerson3(name,age,*,city,xian):
 print("name:",name,"age:",age,"city:",city,"xian",xian) 
printPerson3("QZQ",22,city="XuZhou",xian="SuiNing") #这里命名关键字是city和xian,必须传递参数
#有可能会有疑问，在位置参数中，也可以显示的为参数定义赋值，比如在位置参数中的power3(n=2),
#但是这里命名关键字参数的不同之处是其必须为参数命名，因为相当于dict字典集合中的元素，是key-value形式的
#而位置参数中在不跳过前面的默认参数对后面的默认参数赋值时，是可以省略变量名的

#printPerson3("QZQ",22,"XuZhou","SuiNing")#比如这里就直接传入四个参数，这里默认会把这四个参数都当成位置参数
                                          #但是位置参数只有签名两个name和age,后面的两个是命名关键字参数，必须命名
                                          
def printPerson4(name,age,*,city="镇江",xian):
 print("name:",name,"age:",age,"city:",city,"xian",xian) 
printPerson4("QZQ",22,xian="SuiNing")  #和位置参数一样，如果其中有默认参数，那么也可以这个默认参数可以不写


#6.组合参数
#参数顺序:必选参数、默认参数、可变参数、命名关键字参数和关键字参数

#例子
def f1(a, b, c=0, *args, **kw):
   print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
   
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    
f1(1, 2)                          #   a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)                     #   a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')             #   a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99)       #   a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None)          #   a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}


#神奇的是定义一个tuple或者dict也可以调用上面函数
#将tuple和dict直接传入函数，会分别将其的元素拆分成单个元素值和key-value形式字典对
aa = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*aa, **kw)        #    a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
                     #就相当于调用f1(1, 2, 3, 4,'d': 99, 'x': '#'),这里原aa中剩下的一个元素4就被放在了tuple类型的args中

aa = (1, 2, 3)
kw = {'d': 99, 'x': '#'}
f2(*aa, **kw)        #    a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
                     #就相当于调用f2(1, 2, 3,'d': 99, 'x': '#')