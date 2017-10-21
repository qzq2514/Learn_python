arr=["name1","name2","name3"];
print(arr);                #输出数组list　
print(len(arr));           #输出数组长度，即元素个数
print(arr[0]);            #利用下标索引输出指定数组元素，和C++一样下标从0开始 0~len(arr)-1
print(arr[-3]);           #比较特殊的,python利用负数的下标从后向前取元素,-1~-len(arr)

arr.append("name4");       #append方法在list最后添加元素
print(arr);

arr.insert(1,"name5");      #insert方法在list指定下标位置添加元素，原下标元素及后元素依次后移
print(arr);

var=arr.pop();      #pop方法弹出并删除最后一个元素
print(var);

var=arr.pop(1);      #pop带有整数参数的方法弹出并删除指定下标的元素
print(var);
 
arr[1]="name6";      #替换元素直接用下标访问并重新赋值即可
print(arr);

arrCom=["string",123,True]; #和C++不一样,python的list中元素类型可以不一样
print(arrCom);

arrCom[2]=[1,2,3];       #甚至list中可以再套一个list
print(arrCom);

print(arrCom[2][2]);     #访问list中的list，可以使用类似C++中二维数组下标访问

empty=[];                 #空数组长度为0
print(len(empty));

sortArr=[3,4,7,2,8,3,45];
sortArr.sort();                   #sort方法对list进行排序,这时候就要求list中的元素类型相同,且可比较
print("sortArr:",sortArr);

arrTuple=("tuple1","tuple2","tuple3");  #python还有一种集合tuple,它不可以对其中的元素进行修改，即删除，增加，修改操作
print(arrTuple);                         #也就是tuple不用用类似list的append,insert,pop方法等
print(arrTuple[2]);
print(arrTuple[-2]);                    #但是tuple数组同样可以和list一样使用下标访问元素

tupleEmpty=();                        #定义空tuple
print(len(tupleEmpty));

#但是，要定义一个只有1个元素的tuple，如果你这么定义:
arr1=(34);
print(arr1);
#定义的不是tuple，是34这个整数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，
#这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是34。
#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义

arr1=(34,);        #表示定义一个长度为1的tuple
print(arr1);       #Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号
#同样，定义只包括一个字符串的tuple,也要写成:arr1=("str",);加上逗号，不然就是定义了"str"这个字符串
        
#“可变的”tuple
tupleChange=("name1","name2",[1,2]);
print(tupleChange);
tupleChange[2][0]=3;
tupleChange[2][1]="name3";
tupleChange[2].append("name4");
print(tupleChange);
#表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
#tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，
#指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，
#但指向的这个list本身是可变的！

#即可以对tuple中可变的list进行增删改查等，但是如果这里直接修改tupleChange[2]肯定时错误的
#tupleChange[2]=[3,"name","name4"];这个直接对tuple中的元素赋值，是错误的