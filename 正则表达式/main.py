import re
'''
预备知识:
'-'是特殊字符，在正则表达式中，要用'\'转义
\d可以匹配一个数字，\w可以匹配一个字母或数字

[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）

A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。

^表示行的开头，^\d表示必须以数字开头。

$表示行的结束，\d$表示必须以数字结束。
'''
print(re.match(r'\d{3}\-\d{3,8}','010-12345'))   #匹配-需要转义符号\
print(re.match('\d{3}\-\\d{3,8}','010-12345'))   #如果不用r表示字符串，那么为了表示\还需要一个转义字符，麻烦

print(re.match('\d{3}\-\\d{3,8}','010 12345'))    #匹配成功，match函数返回一个Match对象,否则返回None




print("-----------------------")
#切分字符串
print("a b   c".split(" "))   #一般写法,按照空格来分割字符串，但是不会识别连续的空格
print(re.split(r"\s+","a b   c"))    #\s+表示一个或多个空格
print(re.split(r"[\s\,]+","a,b c,d  e"))  #按照空格或逗号分割
print(re.split(r"[\s\,\;]+","a,b;;c,d  e"))  #按照空格或逗号或分号分割


print("-----------------------")
#字符串分组
'''
除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。比如：
^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：
'''
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))  #这个是原字符串
print(m.group(1))  #原字符串的第一组，即第一个括号中的内容-区号
print(m.group(2))  #原字符串的第二组，即第二个括号中的内容-手机本地号




print("-----------------------")
#贪婪匹配
#需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0
m=re.match(r'^(\d+)(0*)$', '102300')
print(m.groups())    #groups函数将每个组的内容作为tuple的一个元素

#由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
#必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
print(re.match(r'^(\d+?)(0*)$', '102300').groups())




print("-----------------------")
#编译
'''
当我们在Python中使用正则表达式时，re模块内部会干两件事情：
1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
2.用编译后的正则表达式去匹配字符串。
如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，
接下来重复使用时就不需要编译这个步骤了，直接匹配
编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
'''
()
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')  #compile()函数定义一个预编译的正则表达式模板

print(re_telephone.match('010-12345').groups())  #下面用该正则表达式多次匹配字符串，可提高效率
print(re_telephone.match('010-8086').groups())









print("练习1---------------------")
#练习1:
'''
请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
someone@gmail.com
bill.gates@microsoft.com
'''
re_email = re.compile(r'^[a-zA-Z\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$')
def regEmail(email):
   if re_email.match(email):
        print('%s is a correct email!' % email)
   else:
        print('%s is a wrong email!!!!!' % email)


        
regEmail('someone@gmail.com')
regEmail('bill.gates@microsoft.com')
regEmail('someone@gmail.com')
regEmail('bill.gates@microsoft.com')
regEmail('bob#example.com')
regEmail('mr-bob@example.com')
print('ok')



print("练习1---------------------")
#练习2:
'''版本二可以提取出带名字的Email地址：

<Tom Paris> tom@voyager.org => Tom Paris
bob@example.com => bob'''

#尖括号<>也要转义
re_name=re.compile(r'\<*([\w\s]*?)\>*\s*([0-9a-zA-Z.]+)@([0-9a-zA-Z]+)\.([a-zA-Z]{3}$)')
def name_of_email(addr):
    if re_name.match(addr).group(1): #理解下，其实就是如果有尖括号，那么尖括号内的是名字，
        print((re_name.match(addr).group(1)))
    else:                            #没有尖括号，就@前面的都是名字
        print((re_name.match(addr).group(2)))

name_of_email('<Tom Paris> tom@voyager.org')
name_of_email('bob@example.com')














