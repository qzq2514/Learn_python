#为了编写单元测试，我们需要引入Python自带的unittest模块
import unittest
from mydict import Dict

#编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承
class TestDict(unittest.TestCase):


#当运行该测试单元文件的时候，测试类中的所有形如test_xxxx的测试方法都会执行一次,按照字母顺序调用
#setUp,tearDown方法就类似java的JUnit中的before和after,每次运行test_xxxx方法前后都会分别调用setUp,tearDown方法
 def setUp(self):
        print('setUp...')
#以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
 def test_init(self):
  print("test_init执行!!!!")
  d=Dict(a=1,b="test")
  self.assertEqual(d.a,1)                 #单元测试常用的断言就是assertEqual()，判断相等
  self.assertEqual(d.b,"test")
  self.assertTrue(isinstance(d,dict))     #判断返回True
 
 def test_key(self):
  print("test_key执行!!!!")
  d=Dict()
  d["key"]="value"
  self.assertEqual(d.key,"value")
  
 def test_attr(self):
  print("test_attr执行!!!!")
  d=Dict()
  d.key="value"
  self.assertTrue("key" in d)
  self.assertEqual(d["key"],"value")
  
 def test_keyError(self):
  print("test_keyError执行!!!!")
  d=Dict()
  with self.assertRaises(KeyError):      #另一种重要的断言就是期待抛出指定类型的Error，
   print("问题出现:self.assertRaises(KeyError)")  #比如通过d['empty']访问不存在的key时，断言会抛出KeyError
   value=d["empty"]                   #这里的意思是在冒号的后面的语句中期待会出现KeyError异常
                                        #这里我们在Dict类的__getattr__函数定义了访问不存在的key会抛出KeyError异常
   
 def test_attrerror(self):
  print("test_attrerror执行!!!!")
  d = Dict()
  with self.assertRaises(AttributeError):     #点访问属性，会调用__getattr__的方法
   print("问题出现:self.assertRaise(AttributeError)")
   value = d.empty                                                                         
 def tearDown(self):
   print('tearDown...')
   print("----------------------------")
        
#with self.assertRaises(异常类名):后面的语句都会执行，抛出指定的异常才测试通过



#1.运行单元测试最简单的运行方式是在mydict_test.py的最后加上两行代码
#这样就可以把mydict_test.py当做正常的python脚本运行：python3 mydict_test.py
#也就是正常运行python文件
if __name__ == '__main__':
    unittest.main()
   
   
#2.另一种方法是在命令行通过参数-m unittest直接运行单元测试:python3 -m unittest mydict_test