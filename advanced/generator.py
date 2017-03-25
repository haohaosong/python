#-*-coding:utf-8-*-

l = [x*x for x in range(10)]
#for x in l:
#	print(x)

g = (x*x for x in range(10))
#for x in g:
#	print(x)
#普通函数实现fib数列
def fib(max):
	n,a,b=0,0,1
	while(n<max):
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'

#print(fib(10))	

#列表生成器实现fib数列
def fibByGnrl(max):
	n,a,b=0,0,1
	while(n<max):
		yield(b)
		a,b=b,a+b
		n=n+1
	return 'done'

print(fibByGnrl(10))
