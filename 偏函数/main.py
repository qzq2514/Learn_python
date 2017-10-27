#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
print(int("12345"))

#但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
#即参数"12345"是N进制的，输出的是转化为10进制下的数
print(int("12345",base=8))
print(int("12345",base=16))

#假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，
#可以定义一个int2()的函数，默认把base=2传进去
def int2(x, base=2):
    return int(x, base)

#之后就可以用int2函数简单进行大量二进制的转化
print(int2('1000000'))
print(int2('1000001'))
print(int2('1001101'))

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，
#可以直接使用下面的代码创建一个新的函数int2
print("--------------")
import functools
myInt = functools.partial(int, base=2)  #第一参数是函数名
print(myInt('1000000'))
print(myInt('1000001'))
print(myInt('1001101'))


#最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数,上面的例子利用base=2传入键值对型的参数
#也就是myInt = functools.partial(int, base=2)相当于myInt("1100") =int("1100",base=2) 

#下面举一个可能会出错的例子
max2 = functools.partial(max, 10)
print(max2(2,4,2,9,5))
#实际上会把10作为*args的一部分自动加到左边,y也就是相当于上面的max2(2,4,2,9,5)就等于max2(10,2,4,2,9,5)
#所以输出的是10而不是9