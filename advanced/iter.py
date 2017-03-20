#-*-coding:utf-8-*-

#引入collection中的iterator 模块和iterable模块
#Iterator用于判断一个对象是否为迭代器
#Iterable用于判断一个对象能否迭代
from collections import Iterator,Iterable

def g():
	yield 1
	yield 2
	yield 3

#判断能否迭代
print('abc能否迭代?:',isinstance('abc',Iterable))
print('123能否迭代?:',isinstance(123,Iterable))
print('[1,2,3]能否迭代?:',isinstance([1,2,3],Iterable))
print('g()能否迭代?:',isinstance(g(),Iterable))

#判断是否是迭代器
print('abc是否是迭代器?:',isinstance('abc',Iterator))
print('123是否是迭代器?:',isinstance(123,Iterator))
print('[1,2,3]是否是迭代器?:',isinstance('[1,2,3]',Iterator))
print('g()是否是迭代器?:',isinstance(g(),Iterator))
print('iter([1,2,3])是否是迭代器?:',isinstance(iter([1,2,3]),Iterator))

#对list进行迭代
for x in [1,2,3,4,5]:
	print(x)

#对list用iter迭代
for x in iter([1,2,3,4,5]):
	print(x)

#用next打印list
#next(obj)的作用是，将obj指向下一个，但返回的是变化前到值
it = iter([1,2,3,4,5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#定义一个dict
d = {'1号学员':1,'2号学员':2,'3号学员':3}

#以下都是从后向前进行打印
#打印字典中的key值
for k in d.keys():
	print(k)

#打印字典中的value值
for v in d.values():
	print(v)

#打印字典中的key以及value
for k,v in d.items():
	print(k,v)



