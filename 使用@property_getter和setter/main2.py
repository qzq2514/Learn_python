class Student(object):

    @property
    def mybirth(self):
        return self._birth

    @mybirth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
        
s=Student()
s.birth=1996       #赋值和取值，必须使用birth,如果用mybirth,是不会调用def birth(self, value):函数的
                   #那么也就没有_birth属性，这样仅仅是动态绑定了一个普通属性
print(s.birth)     #所以在取值s.age调用def age(self):函数时，没有self._birth会报错
print(s.age)