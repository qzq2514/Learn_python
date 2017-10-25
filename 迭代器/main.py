from collections import Iterable
from collections import Iterator
'''
直接作用于for循环的数据类型有以下几种:
1.集合数据类型，如list、tuple、dict、set、str等；
2.generator，包括生成器和带yield的generator function

这些可以for循环遍历的对象统称为可迭代对象:Iterable
'''
#可以使用isinstance函数判断是不是可迭代对象
print(isinstance("123",(Iterable)))
print(isinstance([],Iterable))
print(isinstance(123,Iterable))

#而其中生成器不但可以用for迭代，还可以用next()函数进行遍历，知道抛出StopIteration异常
print(isinstance((x*x for x in range(10)),Iterable))

#对于可以使用next()函数进行遍历的，我们又叫做迭代器:Iterator
print(isinstance((x*x for x in range(10)),Iterator))

#但是并不是可迭代对象Iterable都是迭代器Iterator
#像list、dict、tuple、str虽然是Iterable，却不是Iterator
print(isinstance((),Iterator))
print(isinstance("123",Iterator))

#将list,dict,tuple,str等可迭代对象变为迭代器可以使用iter()函数
print(isinstance(iter("123"),Iterator))


'''
你可能会问，为什么list、dict、str等数据类型不是Iterator？
这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
'''



'''
小结

凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
'''