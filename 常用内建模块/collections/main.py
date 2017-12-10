#collections是Python内建的一个集合模块，提供了许多有用的集合类。



#namedtuple
from collections import namedtuple
#为了产生一个带坐标的点的类型，只有两个属性-x,y,我们不必麻烦去定义一个类
#我们可以使用namedtuple来定义一个简单的tuple
Point_class=namedtuple("Point",["x","y"])
p=Point_class(2,3)      #注意，Point_class是"类名",参数"Point"只是相当于该"类"描述
print(p.x,p.y)           #可以不用像一般的tuple使用下标来访问元素，namedtuple可以直接用属性

#我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便
print(isinstance(p,Point_class))
print(isinstance(p,tuple))    #看出namedtuple定义的实例p也是tuple

#类似的可以定义一个圆的类型，带有横纵坐标和半径
Circle_class=namedtuple("Circle",["x","y","r"])



print('---------------------------------')
#deque
#python中的list相当于数组，插入和删除元素效率都比较低，deque可以当做栈或队列使用
from collections import deque
d=deque(['a','b','c'])
d.append('d')                #append队尾添加元素
d.appendleft('0')            #appendleft队首添加元素
print(d)
print("pop():",d.pop())      #pop弹出队尾元素
print(d)
print("popleft():",d.popleft()) #popleft弹出队首元素
print(d)




print("--------------------------------")
#defaultdict
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd=defaultdict(lambda :"N/A")
dd['key1']="abc"
print(dd['key1'])     #调用有key的元素，就打印对应的值
print(dd['key2'])     #调用没有key的元素，就打印defaultdict构造函数中lamda的值
#除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的


print("--------------------------------")
#OrderedDict

#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#如果要保持Key的顺序，可以用OrderedDict
from collections import OrderedDict

#这是原dict的两种定义方式:
#1.d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
#2.如下:
d=dict([('Michael',95), ('Bob',75), ('Tracy',85),("Jack",89)])
print(d)         #打印是无序的，每次打印可能顺序都不一样
d=OrderedDict([('Michael',95), ('Bob',75), ('Tracy',85),("Jack",89)])
print(d)         #打印是有序的，这里的顺序并不是按照key的顺序，而是按照元素的顺序，即每次打印都按照相同的排列顺序

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od.keys())   #OrderedDict的key按照元素插入的顺序



#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity    #定义容量

    def __setitem__(self, key, value): #有了该方法，可以使用下标进行插入元素,像下面的
        containsKey = 1 if key in self else 0  #注意这种写法，如果dict中有该key,那么就containsKey=1,没有就赋值为0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)#弹出第一个元素，也就是最先进去的元素,last=True则弹出最后进去的元素
            print('remove:', last)
        if containsKey:
        '''解释下一句:
因为要对以前同key的键值对进行更新，由于FIFO继承于OrderedDict，因此所显示的键值对应该是有序的（同插入顺序）
故，若不用del，则新更新的键值对还在原位置
若用del，将原键值对的引用清除，更新则变为插入，键值对位置在最后
        '''
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

        
dp=LastUpdatedOrderedDict(3)
dp["a"]=1
dp["b"]=2
dp["c"]=3
dp["d"]=4
dp["e"]=5       #设置容量为3,一共对多只能存放3个元素，所以这里的dp["a"]和dp["b"]被删除
print(dp)






print("--------------------------------")
#Counter
#Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c=Counter()
for ch in 'programming':
     c[ch] = c[ch] + 1
print(c)