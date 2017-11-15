#在文件读写那一章节中，我们将内容写入文件中
#但是我们对于数据，内容，我们还可以将其写到内存中，就需要用到StringIO和BytesIO

from io import StringIO

#将一般文本字符串写到内存，需要用到StringIO()函数
#write()函数将字符串写入内存，同时返回写入的字符数
strF=StringIO()
print(strF.write("Hello"))
print(strF.write(" World"))
#getvalue()函数获得内存中的内容
print(strF.getvalue())



print("-----------------")
strR=StringIO("Hello\nQZQ\nMy friend")

#读取StringIO中的内容，像读文件一样就行,readline可以一行一行读
while True:
 s=strR.readline()
 if s=="":
  break
 print(s.strip())