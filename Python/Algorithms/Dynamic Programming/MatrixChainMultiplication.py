from prettytable import PrettyTable 
pr1,pr2=PrettyTable(), PrettyTable()
p,m,b,j,minimum,q,n, name=[5,4,6,2,7], [[0 for i in range(5)] for j in range (5)], [[0 for i in range(5)] for j in range (5)],0,0,0,5, "A"
for d in range(1,n-1):
  for i in range(1,n-d):
    j=i+d
    minimum=float('inf')
    for k in range(i,j):
      q=m[i][k]+m[k+1][j]+(p[i-1]*p[k]*p[j])
      if q<minimum:
        minimum,b[i][j]=q,k
    m[i][j]=minimum
print("Minimum Cost is: ",m[1][n-1])
print("Cost Matrix: ")
pr1.field_names=[i for i in range(5)]
for row in m:
    pr1.add_row(row)
print (pr1.get_string(header=True, border=True))
print("Paranthesization Matrix: ")
pr2.field_names=[i for i in range(5)]
for row in b:
    pr2.add_row(row)
print(pr2.get_string(header=True, border=True))
for i in range(len(b[1])-1,2,-1):
  print('Split occurs at matrix number: ', b[1][i])
def Parenthesize(i,j,n,b):
  global name
  if i==j:
    print(chr(ord(name)),end='')
    name=chr(ord(name)+1)
    return
  print("(",end='')
  Parenthesize(i, b[i][j], n,b)
  Parenthesize(b[i][j] + 1, j,n, b)
  print(")",end='')
Parenthesize(1,n-1,n,b)

