graph=[[0,6,5,5,0,0,0],[0,0,0,0,-1,0,0],[0,-2,0,0,1,0,0],[0,0,-2,0,0,-1,0],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,0]]
cost=[float("inf")]*len(graph)
source=int(input("Enter the source from 0 to "+str(len(graph)-1)+": "))
cost[source]=0

def BF(source):
  for i in range (len(graph)):
      if(graph[source][i]!=0):
        if(cost[i]>cost[source]+graph[source][i]):
          cost[i]=cost[source]+graph[source][i]
          print(cost)
          BF(i)
#driver function
BF(source)
