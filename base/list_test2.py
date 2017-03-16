#-*-coding:utf-8-*-

#对列表函数接口的使用
ls = ['小明','小红','小白','小黑']

#打印列表到函数
def printlist(a):
	for i in a:
		if type(i) is list:
			printlist(i)
		else:
			print(i)

print('-----原列表:')
printlist(ls)

print('-----插入汤姆后:')
ls.insert(1,'汤姆')
printlist(ls)

print('-----弹出最后一个元素:')
ls.pop()
printlist(ls)

print('-----找出汤姆的位置:')
ls.index('汤姆')
printlist(ls)

print('-----反转列表的顺序:')
ls.reverse()
printlist(ls)
