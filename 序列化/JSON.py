#之前我们在main.py中提到，序列化不能在不同语言中传输，如果非要在不同语言中传输
#那我们就要使用更规范的存储方式，像json，他是单纯由字符串构成，可以被任何语言读取
'''
对应关系
JSON类型	 Python类型
{}	         dict
[]	         list
"string"	 str
1234.56	     int或float
true/false	 True/False
null	None
'''
import json
d=dict(name="qzq",age="21",sex="male")
#json.dumps方法返回一个字符串，就是标准的json形式
j=json.dumps(d)
print(j)   #{"age": "21", "sex": "male", "name": "qzq"}


f=open(r"D:\我的编程\newCode\python\序列化\JSONtest.txt","w")
json.dump(j,f)         #同样可以使用json.dump()方法将字符串序列化保存在file-like object中
f.close()


r=open(r"D:\我的编程\newCode\python\序列化\JSONtest.txt","r")
js=json.load(r)         #使用json.load()方法从file-like object中读取json，得到是json字符串
print("反序列化:",js)
#print(js["name"])      #注意：json.load是将file-like object对象变为json字符串，不是直接变为python对象

dd=json.loads(js)        #利用json.loads()方法将json字符串反序列化为python对象
print(dd)
print("name:",dd["name"])

#由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。

