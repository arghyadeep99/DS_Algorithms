from prettytable import PrettyTable

def print_soln(mst):
  table = PrettyTable()
  table.field_names = ['v1', 'v2', 'cost']
  for row in mst:
    table.add_row(row)
  print('minimum spanning tree is')
  print(table)
  cost = sum([row[2] for row in mst])
  print('Cost of MST is:',cost)

def possible(ind):
  if included[graph[ind][0]] or included[graph[ind][1]]:
    return True
  return False

graph = [[0, 1, 28], [0, 5, 10], [1, 2, 16], [1, 6, 14], [2, 3, 12], [6, 3, 18], [6, 4, 24], [5, 4, 25], [4, 3, 22]]

graph = sorted(graph, key = lambda item : item[2])
n = 7

included = [False]*n
mst = list()

included[graph[0][0]] = True
included[graph[0][1]] = True

mst.append(graph.pop(0))

for _ in range(n-2):
  minn = 0
  while(not possible(minn)):
    minn += 1
  included[graph[minn][0]] = True
  included[graph[minn][1]] = True
  mst.append(graph.pop(minn))

print_soln(mst)
