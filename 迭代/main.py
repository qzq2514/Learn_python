from collections import Iterable
#python中的迭代不像C++中for(int i=0;i<n;i++)一样
#它是一种更抽象的迭代形式，对于可迭代的对象都可以使用for var in arr的形式进行迭代
arr={"a":1,"b":2,"c":3}
for var in arr:
 print(var,arr[var])      #dict默认迭代的是键
 
for val in arr.values():  #使用arr.values()来迭代dict对象的值
 print(val)
 
for key,val in arr.items():  #使用arr.items()来同时迭代dict对象的键和值
 print(key,val)
 
str="ABCD"
for ch in str:
 print(ch)         #字符串是一种字符的集合，可以进行迭代
 
print(isinstance("123",Iterable)) #可以使用之前用过的判断变量类型的isinstance函数配上Iterable接口来判断变量是不是可迭代
                                  #使用Iterable要导入:from collections import Iterable
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))

arrList=("jack","rose","jhon")     #对于list和tuple类型，一般的迭代只能直接访问元素
for var in arrList:       
 print(var)

for ind,val in enumerate(arrList): #使用enumerate函数后可以将list或者tuple变成索引-元素值形式的集合
 print(ind,val)                    #就可以利用下标形式来访问元素
 
for val in enumerate(arrList): #enumerate将list或者tuple类型变成索引，元素值形式
 print(val)                    #其中的元素都是(下标,元素值的形式)
 
for x, y in [(1, 1), (2, 4), (3, 9)]:  #这里被遍历的集合就是enumerate形式的，整体是个list集合，
 print(x, y)                           #其中的每个元素是长度为2的tuple,即双元素tuple
 
for x, y,z in [(1,1,2), (2,4,3), (3,6,9)]:  
 print(x,y,z)            #到这里其实我们就可以理解了，其实这里是python的解构赋值，就是把一个tuple赋给多个变量
                         #而上边的enumerate(arrList)是将list或者tuple中的每个元素分别加上各自对应的下标构成一个双元素tuple