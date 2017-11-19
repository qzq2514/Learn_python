#一般我们定义的变量，是保存在内存的，即便我们修改了，当程序运行结束，变量所占用的内存被操作系统回收,
#下次重新运行程序的时候，变量仍然是初始值

#我们把变量从内存中变为可存储或可传输的过程称为序列化，python中称为picking,java等其他语言中可能称为serilazation

import pickle
d=dict(name="qzq",age="21",sex="male")
#pickle.dumps()函数把对象和变量变为bytes,然后我们就可以把bytes存储在文件中
cont=pickle.dumps(d)
print(cont)

print("----------------")
#也可以将对象或者变量直接序列化保存在file-like object中，
f=open(r"D:\我的编程\newCode\python\序列化\test.txt","wb")
pickle.dump(d,f)
f.close()

r=open(r"D:\我的编程\newCode\python\序列化\test.txt","rb")
#用pickle.load()方法将file-like object进行反序列化得到对象或变量
con=pickle.load(r)
r.close()
#打印变量，我们看到变量又回来了，但是要注意的是，这个变量和之前的变量d不是同一个变量，只是内容相同
print(con)

#pickle序列化和其他语言中的序列化一样，其只可用于python语言，且不同版本的python之间不兼容,
#所以用pickle保存一些不是那么重要的数据就行