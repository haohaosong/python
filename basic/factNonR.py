#-*-coding:utf-8-*-

def fact(n):
	if n==0:
		return 0
	ret = 1 
	for i in range(n):
		ret = ret * (i+1)
	return ret
		
for i in range(10):
	print(i,fact(i))
