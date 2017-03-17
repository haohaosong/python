#-*-coding:utf-8-*-

#求fib数列递归解法

def fib(n):
	if n==0:
		return 0
	if n==1:
		return 1
	else:
		result = int(fib(n-1))+int(fib(n-2))
		return result

for i in range(10):
	print(fib(i))
