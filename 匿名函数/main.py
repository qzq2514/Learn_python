
#之前我们用map函数求list中每个元素的平方可以如下:
def pingFang(x):
 return x*x
 
arr=[1,2,3,4,5]
res=map(pingFang,arr)
print(list(res))

#下面使用匿名函数,lambda技术来实现
res=map(lambda var:var*var,arr)
print(list(res))
#其实我们看到lambda var:var*var就类似pingFang求平方函数,
#冒号前面的x表示函数参数,后面是返回值表达式
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果

#此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数

myFunc=lambda var:var*var
print(myFunc(3))

def build(x, y):
    return lambda b: x * x + y * y+b
    
res=build(2,3)(9.5)     
print(res)
'''先是执行build(2,3),返回lamdba,其实就是返回一个函数，这里假设为ff,ff函数相当于
def f(b):
  return 2*2+3*3+b      #这里f中的原lamdba中的x,y在build(2,3)时就已经固定了
之后再执行f(9.5)
最终得到2*2+3*3++9.5
'''

