
#过滤filter函数和map一样，都是传入两个参数，第一个是返回布尔值的函数，还有个就是接受Iterable
#但是不同的是map是把序列中的每个值经过函数映射组成新元素，而filter则是元素传入函数，返回True的才会被保留下来
#也就起到了过滤的作用

#例1:保留list中的偶数
def is_even(x):
 return x%2==0

arr1=[1,2,3,4,5,6,7,8,9,10]
res1=filter(is_even,arr1)
print(list(res1))         #和map函数返回map类型一样，filter返回filter类型，想要打印其中的元素，必须转化为list
                          #即filter()函数返回的是一个Iterator，也就是一个惰性序列，
                          #所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
#例2:保留list中的非空字符串
def notEmpty(ss):
 return ss and ss.strip()   #strip去除字符串两端的连续指定字符，默认是空格

arr2=["A","ac",None,"   ","f",]
res2=filter(notEmpty,arr2)
print(list(res2))


#利用埃氏筛法得到100以内的素数

#首先定义一个生成器，得到所有的奇数
def odd_iter():
 n=1
 while True:
  n+=2
  yield n;
  
def shaiXuan(n):
 return lambda x:x%n>0

#print(shaiXuan(10)(2))     #这里对lambda做个小介绍，lambda其实就是一种匿名函数
                           #这里shaiXuan本身其实是个普通函数，其返回lambda
                           #这时调用shaiXuan也很有意思，10是shaiXuan自己的参数，也就是n=10,
                           #2是lambda的参数，也就是x=2
def prims():
 yield 2               #得到第一个质数2
 nums=odd_iter()       #初始化得带奇数集合
 while True:
  num=next(nums)
  yield num            #新序列的第一个数肯定是质数,直接返回
  nums=filter(shaiXuan(num),nums)    #shaiXuan(num)这里其实就相当于shaiXuan(x)(num),x依次取nums的元素
                                     #其实这里分为两个步骤,先是shaiXuan(x),就是简单调用shaiXuan，返回一个lamdba
                                     #其实也就是返回了个函数，这里假设为f,然后再调用f(num),
                                     #整个过程就相当于执行了return x%num>0

for n in prims():
 if n<100:
  print(n)
 else:
  break
  

#筛选出list中的回文数
#tip:
#s='12345'
#print(s[::-1])    #s[a:b:c]表示在s范围[a,b)内每c个取元素,s[::-1]就可以表示为将s反转
def is_palindrome(n):
 return str(n)==str(n)[::-1]
 
output = filter(is_palindrome, range(1, 1000))
print(list(output))

