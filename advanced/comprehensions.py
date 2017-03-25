#-*-coding:utf-8-*-

#列表生成式的练习
#列表生成式是用来快速的生成list
#简单方便


#利用循环来构造一个list
l = []
for x in range(1,11):
	l.append(x*x)

for x in l:
	print(x)

#利用列表生成式来构造一个list
lc = [x*x for x in range(1,11)if x%2 == 0]

for x in lc:
	print(x)

#用列表生成式来实现全排列
ls = [m+n for m in 'ABC' for n in 'XYZ']

for x in ls:
	print(x)

#用列表生成式来生成key-value
d = { 'x':'1', 'y':'2' ,'z':'3'}
l = [x+'='+y for x,y in d.items()]

for x in l:
	print(x)

#把字符串转换成小写
lslow = ['Apple','IBM',12,'Bit','Bytes',None]

lsl = [s.lower() for s in lslow if isinstance(s,str)==True]

for x in lsl:
	print(x)
