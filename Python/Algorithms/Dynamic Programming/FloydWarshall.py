a=[[0,3,float("inf"),7],[8,0,2,float("inf")],[5,float("inf"),0,1],[2,float("inf"),float("inf"),0]]
def printf(c):
	for i in c:
		print(i)
	print()

def calc(a,k):
	for i in range (len(a)):
		for j in range (len(a)):
			if(a[i][j]>a[i][k]+a[k][j]):
				a[i][j]=a[i][k]+a[k][j]
	printf(a)

for i in range (len(a)):
	calc(a,i)
