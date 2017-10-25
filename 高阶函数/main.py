import math
#abs是取绝对值函数的函数名，也就是函数本身，其可以被赋值给变量，
#换句话说，也就是变量可以指向函数，并之后可以起到和原函数相同的效果
#!!!!其实函数名也就是变量，我们甚至可以对函数名重新赋值,像abs=10将绝对值函数名指向整数(但是一般我们不会这么做)
myAbs=abs
print(myAbs(-129))


#既然函数名也是一种变量，那么其自然也就可以像普通变量一样作为参数传递到函数中
#也就是说函数的参数能够接收别的函数，这就是高阶函数
#函数式编程就是指这种高度抽象的编程范式
def myFunc(a,b,f):
 return f(a)+f(b)


#像这里我们将取绝对值和取平方根函数分别作为参数传递到myFunc函数中
#让myFunc直行不同的操作
print(myFunc(-1,9,abs))
print(myFunc(1,9,math.sqrt))



def str2float(x):
    def char2num(s):
        d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return [d[num] for num in s]
    def fc(x, y):
        return x*10 + y

    L1 = map(char2num, x.split('.')[0])
    L2 = map(char2num, x.split('.')[1])
    return reduce(fc, L1) + reduce(fc,L2) * pow(0.1,len((L2)))