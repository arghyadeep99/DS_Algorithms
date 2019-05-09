s1=input("Enter first string: ")
s2=input("Enter second string: ")
table=[[0 for i in range(len(s2)+1)] for i in range(len(s1)+1)]
def LCS(i,j):
  if(s1[i-1]==s2[j-1]):
    table[i][j]=1+table[i-1][j-1]
  else:
    table[i][j]=max(table[i-1][j],table[i][j-1])

for i in range(1,len(s1)+1):
  for j in range(1,len(s2)+1):
    LCS(i,j)
print("LCS Computation Matrix: ")
for i in table:
  print(*i)

print("Length of LCS is: ",table[len(s1)][len(s2)])
i,j=len(s1),len(s2)
s=''
while i>0 and j>0:
  if table[i][j]!=table[i-1][j]:
    s+=s1[i-1]
    i,j=i-1,j-1
  elif (table[i][j]!=table[i][j-1]):
    s+=s2[j-1]
    i,j=i-1,j-1
  else:
    if(table[i-1][j]>table[i][j-1]):
      i=i-1
    else:
      j=j-1
      
print("The LCS is:",s[::-1])
