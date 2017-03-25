#-*-coding:utf-8-*-

#打印杨辉三角

#用生成式来打印
def trianglePrint(max):
	l = [0,1,0]
	print([1])
	n = 0
	while n < max:
		ll = []
		for x in range(len(l)-1):
			ll.append(l[x]+l[x+1])
		yield(ll)
		l = [0,*ll,0]
		n = n+1
#使用生成式
for x in trianglePrint(10):
	print(x)

#第二种方法
def trianglePrintS(max):
	l = [1]
	n = 0
	while n < max:
		yield l
		l = [1]+[l[x]+l[x+1] for x in range(len(l)-1)]+[1]
		n = n+1

for x in trianglePrintS(10):
	print(x)

