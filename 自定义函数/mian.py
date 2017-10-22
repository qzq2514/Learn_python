from myFunction import myOutAbs;
import math;
def myAbs(x):      #自定义函数格式:   def 函数名(参数):
 if x>=0:
  return x;
 else:
  return -x;

 
print(myAbs(-90.38));
print(myOutAbs(-90.38));   #在利用  from myFunction import myOutAbs  将其他文件中的函数导入后可以使用外面文件的函数

#利用pass定义空函数
def NoneFun():
 pass;  #实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
 
age=20         #同样,pass还可以用于其他语句块中，没有pass就会报错
if age>18:
 pass;
 

 
#print(abs("223"));    #对于我们自定义的函数，如果参数个数出现不匹配，那么会像python的内置函数一样TypeError错误
#print(myAbs("233"));   #但是对于参数类型不匹配，我们自定义的函数就不会报TypeError

def myAbs(x):     
 if not isinstance(x,(int,float)):    #isinstance可以判断变量是不是某种类型之一
  raise TypeError("参数类型错误");    #出现参数类型错误就抛出异常
 if x>=0:
  return x;
 else:
  return -x;
  
#print(myAbs("233"));   

def Move(x,y,step,angle):
 x=x+step*math.cos(angle);
 y=y+step*math.sin(angle);
 return x,y;                          #不像C++一样，python函数可以返回多个变量
 
x,y=Move(10,20,5,math.pi/6);
print(x,y);

ans=Move(10,20,5,math.pi/6);           #这样我们其实可以看到，其实返回多个变量的函数其实返回的就是一个tuple类型
print(ans);


def calcu(a,b,c):
 if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
  return "类型错误";
 if b*b-4*a*c<0:        #次方运算还可以使用**,比如这里b*b可以写成b**2
  return "无解";
 if a==0:
  return -c/b;
 x1=(-b+math.sqrt(b*b-4*a*c))/(2*a);
 x2=(-b-math.sqrt(b*b-4*a*c))/(2*a);
 return x1,x2;

print(calcu(2, 3, "23"));      #类型错误
print(calcu(2, 3, 1));         # => (-0.5, -1.0)
print(calcu(2, 3, 10));        #无解
print(calcu(1, 3, -4));        # => (1.0, -4.0)
print(calcu(0, 2, -4));        #2.0
 