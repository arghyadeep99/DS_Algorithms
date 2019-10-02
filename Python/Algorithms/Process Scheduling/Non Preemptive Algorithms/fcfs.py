from prettytable import PrettyTable
PT=PrettyTable()
n=int(input("Enter number of processes: "))
print("Enter AT values(in ms): ")
AT=list(map(int,input().split()))
print("Enter BT values(in ms): ")
BT=list(map(int,input().split()))
PID=[i for i in range(n)]
CT=[0 for i in range(n)]
TAT,WT=[0 for i in range(n)],[0 for i in range(n)]
CT[0]=AT[0]+BT[0]
for i in range(1,n):
	if CT[i-1]>=AT[i]:
		CT[i]=CT[i-1]+BT[i]
	else:
		CT[i]=AT[i]+BT[i]
TAT=[CT[i]-AT[i] for i in range(n)]
WT=[(TAT[i]-BT[i])*int(TAT[i]>BT[i]) for i in range(n)]
PT.add_column("PID",PID)
PT.add_column("AT",AT)
PT.add_column("BT",BT)
PT.add_column("CT",CT)
PT.add_column("TAT",TAT)
PT.add_column("WT",WT)
PT.add_column("RT",WT)
print(PT.get_string(header=True, border=True))
print("Average TAT:",sum(TAT)/n,"ms.")
print("Average WT:",sum(WT)/n, "ms.")

'''
5
0 15
0 9 
0 3 
0 6 
0 12
'''
