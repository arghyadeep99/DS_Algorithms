class Graph():
  def __init__(self, vertices):
    self.V=vertices
    self.graph=[[0 for col in range(vertices)] for row in range(vertices)]

  def printSolution(self, dist): 
    print ("Vertex \tDistance from Source")
    for node in range(self.V): 
      print (node, "\t\t\t", dist[node])

  def minDistance(self, dist, SPT):
    min = float('inf')
    min_index=0 
    for v in range(self.V): 
        if dist[v] < min and SPT[v] == False: 
            min = dist[v] 
            min_index = v 

    return min_index 

  def dijkstra(self,source):
    dist= [float('inf')] * self.V
    dist[source]=0
    SPT=[False] * self.V

    for _ in range(self.V):
      u=self.minDistance(dist, SPT)
      SPT[u]=True
      for v in range(self.V): 
        if self.graph[u][v] > 0 and SPT[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                dist[v] = dist[u] + self.graph[u][v] 
    self.printSolution(dist)

g=Graph(6)
g.graph=[[0,50,10,0,45,0],[0,0,15,0,10,0],[20,0,0,15,0,0],[0,20,0,0,35,0],[0,0,0,30,0,0],[0,0,0,3,0,0]]

g.dijkstra(0)
