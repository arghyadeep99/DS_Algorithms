import numpy as np
import matplotlib.pyplot as plt
import time, random

x1=[]
x2=[]
y1=[]
y2=[]
inc, n=20,50
mini,maxi,tic,tac,toe=0,0,0,0,0

#Iterative
def IterativeMinMax():
  mini,maxi=arr[0],arr[0]
  for j in range(n):
    if(mini>arr[j]):
      mini=arr[j]
    else:
      maxi=arr[j]
  return mini,maxi
  
  #Recursive
def RecursiveMinMax(low,high):
  if(low==high):
    maxi=mini=arr[high]
    return maxi,mini
  elif(low==high-1):
    return max(arr[low],arr[high]),min(arr[low],arr[high])
  else:
    mid=(low+high)//2
    maxi1,mini1=RecursiveMinMax(low,mid)
    maxi2,mini2=RecursiveMinMax(mid+1,high)
    return max(maxi1,maxi2),min(mini1,mini2)
    
for i in range(10):
  arr=list(range(1,n+1))
  tic=time.time()
  minimum,maximum=IterativeMinMax()
  tac=time.time()
  x1.append(len(arr))
  y1.append((tac-tic)*(10**4))
  recmax,recmin=RecursiveMinMax(0,n-1)
  toe=time.time()
  x2.append(len(arr))
  y2.append((toe-tac)*(10**4))
  print("Iterative Minimum, Maximum: ", minimum, maximum)
  print("Recursive Minimum, Maximum: ", recmin, recmax)
  n=n+5000

plt.ylim((0,5000))
plt.plot(x1, y1, label = 'Iterative Min Max Algorithm')
plt.plot(x2,y2, label='Recursive Min Max Algorithm')
plt.legend()
plt.grid()
plt.xlabel(' Number of Values ')
plt.ylabel(' Time taken per loop(10^-5 s) ')
plt.savefig('graph.png')
