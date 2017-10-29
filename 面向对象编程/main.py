
#简单的class例子

class sutdent(object):
 def __init__(self,name,score):
  self.name=name
  self.score=score
 def print_score(self):
  print("%s %s" % (self.name,self.score))
  
lisa=sutdent('lisa',22)
lisa.print_score()