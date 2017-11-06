
'''
和C++,Java的异常一样，try--except--finally模块,
当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，
则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，
如果有finally语句块，则执行finally语句块(可以没有finally语句)，至此，执行完毕
'''
try:
 print("try:")
 r=10/int('1')
 print("result:",r)
except ValueError as e:                   #try可能出现多种问题，那么就依次捕捉except
 print("ValueError:",e)
except ZeroDivisionError as e:
 print("ZeroDivisionError:",e)
else:                                     #如果没有异常，会执行else语句
 print("No Error")
finally:                                 #一般越特殊的异常放在前面，会依次从上向下的except进行匹配捕捉
 print("finally:")                       #匹配到一个异常，就进入该异常，不会进入其他异常块
print("END")                        #eg.UnicodeError是ValueError的子类，如果ValueError放前面，那么永远不会捕捉到
                                    #UnicodeError,所以从前到后的异常满足:特殊->一般,子类->父类
                                    

                                    
                                    
print("---------------------")                  
'''
使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，
foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理
'''
def foo(s):
 print("foo函数开始")
 r=10/int(s)
 print("foo函数赋值结束")
 return r
def bar(s):
 print("bar函数开始")
 r=foo(s)*2
 print("bar函数赋值结束")
 return r
def main():
 try:
  print("try块开始:")
  r=bar('s')
  print("resule:",r)
 except ZeroDivisionError as e:        #当在foo函数中出现除零或者string转化int异常时
  print("ZeroDivisionError块:")        #foo函数后面和bar函数后面未执行的都不会执行，直接跳到
 except ValueError as e:               #main函数的except异常捕捉
  print("ValueError块:")
 finally:
  print("finally块")
print("END")
main()
print("结束")
'''
调用堆栈:如果上面我们没有在main()函数进行异常捕捉，而是直接调用bar('0'),那么就会一层一层的捕捉异常语句:
main()->bar()->foo(),最后会定位到r=10/int(s)这句话，并抛出ZeroDivisionError除零异常
'''