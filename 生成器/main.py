 #之前介绍列表生成式虽然使用简洁，一行代码就可以生成复杂的list
 #但是他有个缺点，就是列表中的元素必须全部生成才能对这个列表进行操作
 #这样就有个问题，在列表长度非常大时候，会占用大量内存，这样在我们只需要使用列表
 #的前部分元素时候，就会造成后面用不到的元素的空间浪费
 
#解决这个问题，我们使用生成器,其使用非常简单，将列表生成式的中括号改成小括号即可
list1=[x*x for x in range(1,10)]  #这是列表生成式
print(list1)

#方法一
list2=(x*x for x in range(1,10))  #这是生成器generator,将列表生成式的中括号改成小括号即可
print(list2)           #打印生成器我们看到输出的并不是元素，其实它保存的是一种算法，生成元素的算法

print("next",next(list2)) #可以使用next函数来逐个访问生成器中的元素，知道没有元素，就会StopIteration错误
for var in list2:         #常见的我们使用for迭代生成器
 print(var);                  
 
#方法二
#此外，生成器还可以做到列表生成式做不到的事情，比如求斐波那契数列，列表生成式就做不到
#我们可以使用函数简单打印出斐波那契
#因为列表生成式生成的新列表中的元素至于原列表对应位置的元素有关，像x=x*x
#但是斐波那契数列中比如第3个元素
def fib(max):
 n,f1,f2=0,0,1
 while n<max:
  print(f2)
  f1,f2=f2,f1+f2  #同时更新赋值，并不是说f1=f2之后再f2=f1+f2这样其实就相当于f1=2*f2,肯定是不正确的
  n=n+1
 return "done" 
 
fib(6)  #输出前六个斐波那契数测试

def fib_generator(max):
 n,f1,f2=0,0,1
 while n<max:
  yield f2                 #generator生成器的定义形式和函数一样，这里将函数fib中的直接输出print变成yield
  f1,f2=f2,f1+f2           #这时fib_generator就是个生成器
  n=n+1
 return "done"
 
print(fib_generator)     #注意生成器和函数的区别，函数是遇到return才调用结束，而对于生成器，每次next()
                         #或者for循环迭代的时候，那么遇到yield就退出，相当于取到了生成器中的下一个元素
for var in fib_generator(6):  
 print(var)


 
def simple_generator():
 yield "num1"
 yield "num2"
 yield "num3"
 yield 23
 return "结束"
 
for var in simple_generator():  #这里生成一个简单的生成器simple_generator，用for循环迭代我们可以发现
 print(var)                     #该生成器中的元素其实就是每个yield后面值构成的元素的集合
                                #注意这里simple_generator()整体才是一个生成器，小括号不能忘了写
                      

#这里有个小问题，我们用for迭代生成器，永远不会拿到生成器中return中的值，如果非要拿到
#那么就要捕捉StopIteration异常,例如这里捕捉simple_generator()生成器的return值

gen=simple_generator()
n=0;
while True:
 try:
  #x=next(simple_generator())        #不能这样写，不然每次都是一个新的生成器，无线循环打印num1
  x=next(gen)
  print("simple_generator[%d]:%s" % (n,x))
  n=n+1
 except StopIteration as e :
  print("return值:",e.value) 
  break
  
 
print("测试加号拼接list:",[2,3,4]+["2","3","4"])  #list直接通过+号进行拼接


#打印杨辉三角形:
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1] #两端都是1,list直接通过+号进行拼接

n=0
for t in triangles():
    print(t)
    n+=1
    if n==10:
        break
        
                                