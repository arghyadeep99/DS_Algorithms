#O(n) implementation of Merge Sort in Python for best and worst case scenario. (Worst~1000 cases)

def merge_sort(LIST):
    start = []
    end = []
    while len(LIST) > 1:
        a = min(LIST)
        b = max(LIST)
        start.append(a)
        end.append(b)
        LIST.remove(a)
        LIST.remove(b)
    if LIST: start.append(LIST[0])
    end.reverse()
    return (start + end)

arr=[3,0,1,8,7,2,5,4,9,6]
print(merge_sort(arr))
