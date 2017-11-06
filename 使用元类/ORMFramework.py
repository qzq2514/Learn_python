'''
让我们来尝试编写一个ORM框架。
编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，
想定义一个User类来操作对应的数据库表User，我们期待他写出这样的代码
'''
'''class User(Model):
 id=IntegerField('id')
 name=StringField('username')
 email=StringField('email')
 password=StringField('password')'''
 
#首先来定义Field类，它负责保存数据库表的字段名和字段类型
class Field(object):
  def __init__(self,name,column_type):
   self.name=name
   self.column_type=column_type
  def __str__():
   return '<%s:%s>' % (self.__class__.__name__,self.name)
   
#在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等
class IntegerField(Field):
 def __init__(self,name):
  super(IntegerField,self).__init__(name, 'bigint')
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')