from prettytable import PrettyTable
pr1=PrettyTable()
stages,minimum,n=4,float('inf'),8
cost,d,path,=[0 for i in range(9)],[0 for i in range(9)],[0 for i in range(9)]
graph=[[0,0,0,0,0,0,0,0,0],[0,0,2,1,3,0,0,0,0],[0,0,0,0,0,2,3,0,0],[0,0,0,0,0,6,7,0,0],[0,0,0,0,0,6,8,9,0],[0,0,0,0,0,0,0,0,6],[0,0,0,0,0,0,0,0,4],[0,0,0,0,0,0,0,0,5],[0,0,0,0,0,0,0,0,0]]
for i in range(n-1,0,-1):
  minimum=float('inf')
  for k in range(i+1,n+1):
    if graph[i][k]!=0 and graph[i][k]+cost[k]<minimum:
      minimum=graph[i][k]+cost[k]
      d[i]=k
  cost[i]=minimum
pr1.field_names=['Vertex','Cost','Destination']
zipped=list(zip(list(i for i in range(9)), cost,d))
for row in zipped:
    pr1.add_row(row)
print (pr1.get_string(header=True, border=True))
path[1],path[stages]=1,n
for i in range(2,stages):
  path[i]=d[path[i-1]]
print('The path is: ')
for i in range(1,stages):
  print(path[i],'->', end=' ')
print(path[stages])
