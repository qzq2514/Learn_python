#datetime是Python处理日期和时间的标准库。

'''
注意到datetime是模块，datetime模块还包含一个datetime类，
通过from datetime import datetime导入的才是datetime这个类。
如果仅导入import datetime，则必须引用全名datetime.datetime
'''
from datetime import datetime
now=datetime.now()   #得到当前时间
print(now)
print(type(now))     #datetime.datetime类型



d=datetime(2017,12,8,22,36,23)   #自定义时间
print(d)



print("--------------------------------")
#datetime转换为timestamp
'''在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp

timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，
这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的
（假定时间已校准）

eg.timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
换到北京时间:timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
'''

#timestamp()函数将datetime型日期转换到timestamp
#Python的timestamp是一个浮点数,如果有小数位，小数位表示毫秒数
print(d.timestamp())  #1512743783.0



print("--------------------------------")
#timestamp转换为datetime
print(datetime.fromtimestamp(1512743783.0))
'''
注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。
本地时间是指当前操作系统设定的时区。

例如北京时区是东8区，则本地时间：
2015-04-19 12:20:00
实际上就是UTC+8:00时区的时间：
2015-04-19 12:20:00 UTC+8:00
而此刻的格林威治标准时间与北京时间差了8小时，也就是UTC+0:00时区的时间应该是：
2015-04-19 04:20:00 UTC+0:00'''


#timestamp也可以直接被转换到UTC标准时区的时间:
print("本地时间:",datetime.fromtimestamp(1512743783.0)) # 本地时间
print("UTC时间:",datetime.utcfromtimestamp(1512743783.0))  #UTC时间,可以看到其与本地的北京时间相差了8个小时


print("--------------------------------")
#str转换为datetime:
#strptime给定字符串的时间和指定形式(%Y-%m-%d %H:%M:%S)
#!!!!注意转换后的datetime是没有时区信息的!!!
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')  
print(cday)


print("--------------------------------")
#datetime转换为str:
now=datetime(2017,12,8,22,36,23)
print("datetime转换为str下时间",now)
#指定位置输出日期指定的内容指定:%Y %m %d %H %M %S分别是年月日时分秒(均是数值型),%b %a是字符型的月日:Fri, Dec
print(now.strftime('%a, %b %S %H:%M'))  





print("--------------------------------")
#日期时间加减:
'''
对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
加减可以直接用+和-运算符，不过需要导入timedelta这个类
'''
from datetime import timedelta
now = datetime(2017,12,8,22,36,23)
print(now)
print(now + timedelta(hours=10))          #加十个小时
print(now - timedelta(days=1))            #减一天
print(now + timedelta(days=2, hours=12))  #加2天12个小时




print("--------------------------------")
#本地时间转换为UTC时间
'''
本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，
除非强行给datetime设置一个时区
'''
from datetime import datetime, timedelta, timezone
tz_utc_7 = timezone(timedelta(hours=7)) # 创建时区UTC+7:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_7) # 强制设置为UTC+7:00
#replace()只是在给定的日期后面添加时区，日期是不会变的
#就是强制的时区转化
print(dt)  #这里会在日期后面加一个"+07:00"表明这时第7时区


print("--------------------------------")
#时区转换
#utcnow()函数获得UTC时间(用当前系统时间减去系统时区)
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)   #拿到UTC时间，并强制设置时区为UTC+0:00:
print(utc_dt)  #15:16:52.096285+00:00
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  # astimezone()将UTC时区转换为北京时间:
print(bj_dt)   #23:16:52.096285+08:00
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9))) # astimezone()将UTC时区转换为东京时间:
print(tokyo_dt)#00:16:52.096285+09:00
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9))) # astimezone()将北京时间转换时区为东京时间:
print(tokyo_dt2)#00:16:52.096285+09:00
#其实就是根据两地的时区差来进行时区转换
'''
时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换
'''






print("练习--------------------------------")
#练习:
#假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，
#均是str，请编写一个函数将其转换为timestamp
import re
def to_timestamp(dt_str, tz_str):
    tz_re = re.compile(r'^UTC([+-][0-9]+)\:00')    
    tz_hours = int(re.match(tz_re, tz_str).group(1))  #根据代表时区字符串(例如'UTC+7:00')来获取时区差
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S') #根据传入的日期字符串获得对应的datetime型日期
    #将该日期指定为对应的时区(时间),replace()只是在给定的日期后面添加时区，日期是不会变的
    dt = dt.replace(tzinfo=timezone(timedelta(hours = tz_hours)))  
    return dt.timestamp()
 
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')  
print(t1) #1433121030.0
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print(t2) #1433121030.0
#t1,t2其实同一个时刻，只是在不同的时区，如果转化到UTC，都是一样的,所以其timestamp也是一样的
