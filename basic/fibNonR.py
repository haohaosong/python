#-*-coding:utf-8-*-

def fibNonR(n):
	if n==0:
		return 0
	if n==1:
		return 1
	f1 = 0
	f2 = 1
	fret = int()
	
	for i in range(n-1):
		fret = f1+f2
		f1 = f2
		f2 = fret

	return int(fret)

for x in range(10):
	print(fibNonR(x))
