from prettytable import PrettyTable

def priority(processes):
    
    temp_store = [] 
    time, idle = 0, []
    while processes:
        temp = [process for process in processes if process[1] <= time]
        temp.sort(key=lambda x: x[-1]) #Sort by priority
        if temp:
            # If two processes have same priority then checking AT else PID
            curr_proc = temp[0]
            for item in temp:
                if item[3] == curr_proc[3]:
                    if item[1] < curr_proc[1] or (item[1] == curr_proc[1] and item[0] < curr_proc[0]):
                        curr_proc = item

            temp_store.append((curr_proc[0], time, time + curr_proc[2]))
            processes.remove(curr_proc)
            time += curr_proc[2]
        else:
            idle.append((time, time+1))
            time += 1
    
    at, bt, ct, tat, wt = [], [], [], [], []
    for i in range(n):
        at.append(dict_proc[i+1][0])
        bt.append(dict_proc[i+1][1])
        ct.append([item[2] for item in temp_store if item[0] == i+1][0])
        tat.append(ct[-1] - at[-1])
        wt.append(tat[-1] - bt[-1])

    total = temp_store[-1][2]

    return temp_store, at, bt, ct, tat, wt, total, idle
	
def sasta_printer(at, bt, ct, tat, wt, total, idle,prior):

    table = PrettyTable(['PID', 'AT', 'BT', 'Priority','CT', 'TAT', 'WT'])
    for i in range(n):
        table.add_row([i+1, at[i], bt[i], prior[i],ct[i], tat[i], wt[i]])
    print(table)
    for time in idle:
        print('CPU idle from {} to {}'.format(time[0], time[1]))
    print('Total time:', total)
    print("Idle time of CPU: ",sum(idle[i][1]-idle[i][0] for i in range(len(idle))))
    print('Average Turnaround time:', sum(tat) / n)
    print('Average Waiting time:', sum(wt) / n)
    
n = int(input('Enter no of processes: '))

dict_proc = {}
processes,priorities = [],[]
for i in range(n):
    at, bt, prior = map(int, input('Enter AT, BT and priority for {}: '.format(i+1)).split())
    priorities.append(prior)    
    # format -> PID, AT, BT, Priority
    processes.append([i+1, at, bt, prior])     
    dict_proc[i+1] = (at, bt, prior)

print('\nPriority non-preemptive:')
_, at, bt, ct, tat, wt, total, idle = priority(processes[::])
sasta_printer(at, bt, ct, tat, wt, total, idle,priorities)

'''
5
0 15 6
5 9 3
6 3 7
8 6 9
10 12 4
'''
