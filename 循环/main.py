names=["name1","name2","name3"];
for name in names:
 print("Hello,%s" % name);


#循环计算0~9和
sum=0;
for x in list(range(10)):      #range()函数，可以生成一个整数序列
 sum+=x;                       #再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数
print(sum);

sum=0;
ind=0;
while ind<10:
 sum+=ind;
 ind+=1;                      #python中没有自增运算，变量加一就用 +=1 操作
print(ind);                   #因为python是基于内容的，不是像C++一样基于变量的，所以当a=5,b=5时候
                              #a,b变量的地址是相同(可以用id(a)进行地址查看)，所以直接a++会影响到b，
                              #所以这里用a=a+1或者a+=1,这时再查看a的地址，其实可以发现a的地址变化了
                              
i=1;                              
while i<10:
 if i==6 :       #i==6时就跳出循环整个循环，所以这里只会输出1,2,3,4,5
  break;
 print(i);
 i+=1;
print("------------");
i=0;                              
while i<10:
 i+=1;
 if i==6 :       #i==6时就跳出这里i=6的循环，继续开始下面i=7的循环,所以这里只会输出1,2,3,4,5,7,8,9,10
  continue;
 print(i);
 