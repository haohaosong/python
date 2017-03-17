#-*-coding:utf-8-*-

def factR(n):
	if n==0:
		return 0
	if n==1:
		return 1
	else:
		ret = n*int(factR(n-1))
		return ret

for i in range(10):
	print(i,factR(i))
