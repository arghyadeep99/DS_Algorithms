from prettytable import PrettyTable
def rr(processes):
	
	tq = int(input('Enter time quantile: '))
	
	temp_store, idle, rq= [], [], []
	
	time = min([process[1] for process in processes])
	rq.extend([process[::] for process in processes if process[1] <= time])
	idle.append((0, time))

	while rq:
		curr = rq.pop(0)
		if curr[2] <= tq:
			temp_store.append([curr[0], time, time + curr[2]])
			time += curr[2]
			processes.remove(curr)				
			present = [x[0] for x in rq]
			present.append(curr[0])
			rq.extend(sorted([process[::] for process in processes if process[1] <= time and (not process[0] in present)], key=lambda x: x[1]))
		else:
			temp_store.append([curr[0], time, time + tq])
			time += tq
			processes[processes.index(curr)][2] -= tq
			curr[2] -= tq
			present = [x[0] for x in rq]
			present.append(curr[0])
			rq.extend(sorted([process[::] for process in processes if process[1] <= time and (not process[0] in present)], key=lambda x: x[1]))
			rq.append(curr)

	ct = [0] * n
	at, bt, tat, wt, rt = [], [], [], [], []
	for i in range(len(temp_store)):
		ct[temp_store[i][0]-1] = temp_store[i][2]

	for i in range(n):
		at.append(dict_proc[i+1][0])
		bt.append(dict_proc[i+1][1])
		tat.append(ct[i] - at[-1])
		wt.append(tat[-1] - bt[-1])

	total = temp_store[-1][2]

	return temp_store, at, bt, ct, tat, wt, total, idle

def sasta_printer(at, bt, ct, tat, wt, total, idle):

    table = PrettyTable(['PID', 'AT', 'BT','CT', 'TAT', 'WT'])
    for i in range(n):
        table.add_row([i+1, at[i], bt[i],ct[i], tat[i], wt[i]])
    print(table)
    for time in idle:
        print('CPU idle from {} to {}'.format(time[0], time[1]))
    print('Total time:', total)
    print("Idle time of CPU: ",sum(idle[i][1]-idle[i][0] for i in range(len(idle))))
    print('Average Turnaround time:', sum(tat) / n)
    print('Average Waiting time:', sum(wt) / n)
    
n = int(input('Enter no of processes: '))

dict_proc = {}
processes = []
for i in range(n):
    at, bt = map(int, input('Enter AT, BT for {}: '.format(i+1)).split())   
    # format -> PID, AT, BT
    processes.append([i+1, at, bt])     
    dict_proc[i+1] = (at, bt)

print('\nRound Robin Scheduling:')
_, at, bt, ct, tat, wt, total, idle = rr(processes[::])
sasta_printer(at, bt, ct, tat, wt, total, idle)

'''
5
0 15
0 9 
0 3 
0 6 
0 12
'''
