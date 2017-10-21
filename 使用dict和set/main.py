dic={"name1":12, "name2":23, "name3":34, 34:"name5"};       #dict类型是字典集合，就类似于C++中的map
print(dic["name1"]);               #键值对的映射可以是不同类型，键之间可以类型不同，值之间类型也可以不同
print(dic[34]);
print(dic);

dic["name4"]=90;      #可以使用下标赋值的方法在dict集合中进行插入
print(dic);

dic["name4"]=89;      #一个键之对应一个值，所以相同的键，后赋值的键值会覆盖之前赋值的
print(dic["name4"]);

#print(dic["name6"]);         #访问未赋值或不存在的键对应的值，会报错
print("name6" in dic);        #解决1.在访问dict类型集合的元素时，可以使用in关键字进行提前判断
print(dic.get("name6"));      #解决2.通过dict提供的get方法，如果key不存在，可以返回None，或者已经指定的value

print(dic.pop("name2"));      #pop()方法利用键删除键值对
print(dic);

'''
和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，
需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。
这个通过key计算位置的算法称为哈希算法（Hash）

综上：要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，
可以放心地作为key。而list是可变的，就不能作为key
'''

#注意,python中的set仅仅表示一个集合，无序，无重复,定义时用set([])形式
#set()是个函数，将其list类型的参数转为set类型
s=set([3,2,1]); #注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，
print(s);    #显示的顺序也不表示set是有序的

s=set([2,3,2,4,9,8,4,4]);#重复元素在set中自动被过滤
print(s); 

s.add(7);       #通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
print(s); 
s.add(7);
print("s:",s);

s2=set([10,1,2,4,6,7,8]);
print("s2:",s2);
print("s&s2:",s&s2);          #就像数学中的集合一样，python中的集合可以使用&,|进行交并运算
print("s|s2:",s|s2);


#思考
tup1 = (1,2,3)      #纯tuple类型，不可变
tup2 = (1,[2,3,4])  #非纯tuple,其含有可变list元素
#mydict = {tup1:'tup1',tup2:'tup2'} #==>unhashable type: 'list'
mydict = {tup1:'tup1'}            #不包含list元素的tuple变量可以用来构造dict集合和set集合
myset1 = set(tup1)                #因为,dict的键和set中的元素都必须是不可变元素
mydict = {tup1:'tup1','tup2':tup2}#注意，可变元素可以做dict集合的值,因为值不要求不可变
#myset2 = set([tup1,tup2]) #==>unhashable type: 'list'
print(mydict[tup1])
print(myset1)
#print(myset2)
