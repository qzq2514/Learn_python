
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