list1=list(range(1,11)) #生成简单的整数list，可以直接用range
print(list1)

#如果想生成[1*1,2*2,3*3.....10*10]这种比较复杂的list,最简单的就是想到循环迭代的方法
list2=[]
for var in range(1,11):
 list2.append(var*var)
print(list2)

#但是这种循环的方法还是比较繁杂，下面使用一行语句完成相同的操作
list3=[var*var for var in range(1,11)];  #生成元素表达式子放在for前面，之后就是简单的for迭代
print(list3)

list4=[var*var for var in range(1,11) if var%2==0];  #在for之后还可以使用for循环进行比较复杂的判断
print(list4)                                         #这里将1~10之间偶数的平方进行计算组成list

list5=[m+n for m in "ABC" for n in "MNZ"]   #两层循环生成新列表list
print(list5)

list6=[m+n for m in range(1,7) for n in range(11,17) if n%2==0 and m%2==0]   #两层循环加判断生成新列表list
print(list6)

import os
dirs=[d for d in os.listdir(r'D:\我的编程\newCode\python')]
print(dirs)

arrDict={"a":1,"b":2,"c":3}                #在《迭代》那一节我们看到了for循环可以同时遍历两个变量
list7=[k+'='+str(v) for k,v in arrDict.items()] #所以在列表生成中可以两个变量的for(不同于上边的两个for循环)
print(list7)

L = ['Hello', 'World', 18, 'Apple', None]        #输出list中的字符串的小写形式
judge1=[s.lower() for s in L if isinstance(s,(str))]
print(judge1)

judge2=[True if isinstance(s,(str)) else False for s in L ]
print(judge2)

#注意这里两种形式的列表生成，judge1把if判断写在for循环后面，起到了过滤的作用
#第二种把if写在for前面，并不能算是过滤，其实就是一种计算,judge2其实就相当于下面代码:

def f(x):
 if isinstance(x,(str)):
  return True
 else:
  return False
  
judge2=[f(s) for s in L ]
print(judge2)

#所以第一种judge1可以只写if不写else,起到过滤作用，满足if的就放在列表生成的新列表中
#但是第二种judge2就必须把if和else都写，因为不写else相当于在函数f(x)中没有x不是字符串的情况下返回值
#这是违反函数的规则的:函数必须有明确的返回值