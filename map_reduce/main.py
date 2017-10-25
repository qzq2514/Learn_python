from functools import reduce
def func(x):
 return x**2

#map()函数接收两个参数，函数和可迭代对象Iterable
#map的作用是将函数依次作用在Iterable中的每个元素生成新元素，并返回一个Iterator
r=map(func,[1,2,3,4,5])
#这里利用list()将"懒惰"的Iterator转化为list以便全部输出
print(list(r))

#map()作为高阶函数，事实上它把运算规则抽象了
#下面用一行代码将list中的整数变为字符串构成新列表
print(list(map(str,[12,23,345])))


#reduce()就收两个参数，一个函数(该参数必须接受两个)和一个Iterable,reduce函数的作用是将其参数的函数依次作用到Iterable,将得到的结果
#和序列中的下一个元素作为两个参数再次放在reduce的参数函数中调用
#形象说:reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#下面是一个用reduce求序列和的例子
def add(x,y):
 return x+y

res=reduce(add,[1,2,3,4,5])
print(res)

#这是一个将[1,2,3,4,5]变为整数12345的例子
def change(x,y):
 return x*10+y
res=reduce(change,[1,2,3,4,5])
print(res)


#这里演示一个将字符串转化为整数的例子
def change(x,y):
 return x*10+y
res=reduce(change,[1,2,3,4,5])

def char2int(x):
 return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[x]

res=reduce(change,map(char2int,"87937409"))      #这里可以仔细想想map_reduce的巧妙之处
print(res)

#整理成一个str2int的函数就是：
def str2int1(s):
    def change(x, y):
        return x * 10 + y
    def char2int(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(change, map(char2int, s))
    
print(str2int1("834927"))

#使用后面的更高级特性lamda:
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
    
print(str2int2("834927"))


'''练习1:
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
'''
def normalize(ss):
 return ss[0].upper()+ss[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

'''练习2:
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
'''
def prod(l):
 def multiply(x,y):
  return x*y
 return reduce(multiply,l)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

'''练习3:
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
'''

#我自己的方法
def myStr2float(ss):
 def char2int(ch):
  return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ch]
 def change(x,y):
  return x*10+y;
 l1=reduce(change,map(char2int,ss.split(".")[0]))  #split将字符串进行分割，组成数组
 l2=reduce(change,map(char2int,ss.split(".")[1]))  #l1,l2分别是小数点前和小数点后的数字
 return l1+l2*pow(0.1,len(str(l2)))
  
print('str2float(\'123.456\') =', myStr2float('123.456'))


#评论里的答案:
def str2float(x): 
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    def fc(x, y):
        return x*10 + y

    L1 = map(char2num, x.split(".")[0])
    L2 = map(char2num, x.split(".")[1])
    l1=reduce(fc,L1);
    l2=reduce(fc,L2);
    return l1 + l2 * pow(0.1,len(str(l2)))   #评论里直接len(L2)是错误的，L2是map类型，没有长度
    
print('str2float(\'123.456\') =', str2float('123.456'))