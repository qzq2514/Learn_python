from enum import Enum,unique
Month =Enum('month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

#Enum默认值从1开始
for name,member in Month.__members__.items():
 print(name, '=>', member, ',', member.value)
#Jan => month.Jan , 1

print(Month.Jan)
#print(month.Jan)   错误
print(Month.Jan.value)



#精确控制枚举元素的值，自定义类，从Enum继承
@unique
class Weekday(Enum):
  sun = 0
  Mon = 1
  Tue = 2
  Wed = 3
  Thu = 4
  Fri = 55
  Sat = 66

#多种访问方式:
print(Weekday.sun)
print(Weekday['sun'])
print(Weekday.Mon.value)
print(Weekday['sun'].value)

day1=Weekday.sun
print(day1==Weekday.Tue)

print(Weekday(1))      #根据元素值得到enum元素
print(Weekday(55))
#print(Weekday(6))     #没有值的对应的enum元素，报错


#直接通过点，下标访问等都是返回"类名.枚举元素名"形式的常量，除非再加上.value才得到enum元素对应的值
  
  