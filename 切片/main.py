arr=["name1","name2","name3","name4","name5","name6"]

print(arr[0:4]);  #切片就是为了取指定索引范围的操作，0~4表示下标前闭后开区间
print(arr[:4]);   #从下标为0开始索引，可以省略0

print(arr[-3:-1]); #python下标可以为负，这里表示从后往前取，-1表示最后一个元素，-3表示倒数第3个元素，同样前闭后开
print(arr[-3:]);   #表示取包括倒数第三个之后的所有元素


L = list(range(100))
print(L[0:10])    #取前十个
print(L[-10:])    #取后十个
print(L[:10:2])   #前十个数，每两个取一个,第一个取
print(L[::10])    #所有数，每十个取一个,第一个取
print(L[:])      #取所有元素,和print(L)效果一样


arrTuple=(2,3,4,5,6,7)
print(arrTuple[:3])   #arrTuple也是一种list,也可以使用切片，得到的还是tuple

str="myNameisQZQ"
print(str[::2])      #字符串也可以看成list，其每个元素就是其中的每个字符，所以其也可以使用切片