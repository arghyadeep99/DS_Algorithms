pw,cap,n=[[1,2],[2,3],[5,4],[6,5]],8,4
table=[[0 for x in range(cap+1)] for x in range(n+1)]
for i in range(1,n+1):
  for j in range(cap+1):
    if pw[i-1][1]<=j:
      table[i][j]=max(table[i-1][j], table[i-1][j-pw[i-1][1]]+pw[i-1][0])
    else:
      table[i][j]=table[i-1][j]
for i in table:
  print(*i, sep=' ')
i,j,sack=n,cap,[]
while i>0 and j>0:
  if table[i][j]!=table[i-1][j]:
    sack.append(i)
    i,j=i-1,j-pw[i-1][1]
  else:
    i=i-1
print('Items added are: \nItem no.\tWeight\t Profit')
for i in sack:
  print(i,'\t\t',pw[i-1][1],'\t',pw[i-1][0])
