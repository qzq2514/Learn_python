
#sorted对可比较的元素进行排序
print(sorted([12,3,52,87,43,9,10]))

#此外sorted还是个高阶函数，也就是可以接受函数作为参数
#这里将list中的元素按绝对值进行比较排序
#内部步骤是:将list中的元素传入key函数中，然后对函数返回值进行比较排序,
#但是要注意，最终返回的是key函数返回值对应位置元素的排序，并不是返回值的排序
print(sorted([12,-3,-52,87,43,-9,10],key=abs))

#这里对字符串忽略大小写进行排序,不然的话大写是全部小于小写的,即代表的'Z'<'a'
strs=['bob', 'About', 'zoo', 'Credit']
print(sorted(strs,key=str.lower))


#默认从小到达排序，想进行反序排序，使用reverse=True参数
print(sorted(strs,key=str.lower,reverse=True))


#练习:
#假设我们用一组tuple表示学生名字和成绩：
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：

#要注意sorded的参数函数，其接受的是list中的元素，
#所以其实by_name接受的是L中的每个元素，像('Bob', 75)或('Adam', 92)等等
#所以这里的每个元素是tuple
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
 return t[0]#我们按照名字排序，就直接返回学生的名字

def by_score(t):
 return t[1]#我们按照名字排序，就直接返回学生的名字
 
name_sorted = sorted(L, key=by_name)
score_sorted = sorted(L, key=by_score)
print("按名字排序:",name_sorted)
print("按成绩排序:",score_sorted)