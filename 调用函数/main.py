print(abs(12));             #求绝对值函数
print(abs(-12));            #传入的参数数量不对,或者参数类型不能被函数所接受，会报TypeError的错误
print(abs(-12.89));


print(max(2,3,-12,90));      #函数max()可以接收任意多个参数，并返回最大的那个

print(int('123'));                  #类型强制转化函数
print(float('123.8'));
print(str('123.8'));
print(bool(1));
print(bool(""));                   #整数0,空字符串""或者空参数都返回False

myAbs=abs                            #像变量一样，可以对函数名进行重新定义赋值
print(myAbs(-9084.89));

n1=255;
n2=1000;
print(str(hex(n1)));      #hex()函数转化为十六进制
print(str(hex(n2)));
#print(str(hex(9.8)));     #hex传入整数

print(sum([1, 2, 3]))          #对list元素求和