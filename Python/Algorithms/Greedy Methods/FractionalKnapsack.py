IPW=[[1,10,2],[2,5,3],[3,15,5],[4,7,7],[5,6,1],[6,18,4],[7,3,1]]

PbyW=sorted(IPW,key=lambda v:v[1]/v[2],reverse=True)
print(PbyW)
capacity=15
profit=0
items,par_item=[],[]
for sublist in PbyW:
  if(sublist[-1]<=capacity):
    capacity-=sublist[-1]
    profit+=sublist[1]
    items.append(sublist[0])
  else:
    fraction=capacity/sublist[2]
    profit+=sublist[1]*fraction
    par_item.append(sublist[0])
    break
print("Maximum profit:",profit)
print("Fully added items:",items)
print("Partially added item:",par_item)
