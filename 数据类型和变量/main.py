print("I\'m \"Ok\"");    ##"\"进行转义
print(r"I\'m \"Ok\"");   ##前面加个r，则""中的内容原样输出不变化

print('''Line1
Line2
line3''');              ##多行输出，好看的话可以用'''内容'''符号
print('Line1\nLine2\nline3'); ##直接用\n换行符号，和上面输出结果是一样的

print(10/3);             ##python中有两种除法，/是输出小数,//是和C++一样整除
print(10//3);