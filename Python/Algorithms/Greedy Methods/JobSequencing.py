prof_dl=[[1,3,1],[2,5,3],[3,20,4],[4,18,3],[5,0,2],[6,6,1],[7,30,2]]
def sequencing(prof_dl):
  job_size=(max(prof_dl, key=lambda x: x[2]))[2]
  profit=[0]*job_size
  isEmpty,job_seq=[True]*job_size,['']*job_size
  prof_dl=sorted(prof_dl, key= lambda x: x[1],reverse=True)
  for i in range(len(prof_dl)):
    for j in range(min(job_size-1,prof_dl[i][2]-1),-1,-1): 
      if isEmpty[j] is True:
        isEmpty[j],profit[j],job_seq[j]=False,prof_dl[i][1],prof_dl[i][0]
        break    
  print('Jobs\tSlot\tProfit')
  for i in range(job_size):
    print( ' ',job_seq[i],'\t',i+1,'\t\t',profit[i])
  print('Profit is: ',sum(profit))
sequencing(prof_dl)

