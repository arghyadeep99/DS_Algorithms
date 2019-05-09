states={0:"Maharashtra", 1:"Goa", 2:"Karnataka", 3:"Gujarat", 4:"Chattisgarh", 5:"Odisha", 6:"Bengal"}
graph={0:[1,2,3,4], 1:[0,2], 2:[0,1], 3:[0], 4:[0,5], 5:[4,6], 6:[5]}
colors=["Red", "Green", "Blue"]
col_graph,j={},1

def check(state, colour):
	global graph
	global col_graph
	for i in graph[state]:
		if i in col_graph and col_graph[i]==colour:
			return False
	return True

def assign(state, colour):
	global col_graph
	col_graph[state]=colour

def solve(vertex):
  i=0
  global j
  if vertex==7:
    print('Solution ',j,':\n')
    for key, value in col_graph.items():
      print(states[key] + " : " + colors[value])
      if(states[key]=='Bengal'):
        print('\n')
    j=j+1
    return False
  for i in range(len(colors)):
    if check(vertex,i)==True:
      assign(vertex,i)
      if solve(vertex+1)==True:
        return True
      assign(vertex,0)
solve(0)
