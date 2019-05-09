import random
global k
k=1
def QuickSort(arr, low, high):
    if low<high:
      p_index=Partition(arr, low, high)
      QuickSort(arr,low,p_index-1)
      QuickSort(arr,p_index+1,high)

def Partition(arr,low,high):
  global k 
  r=random.randrange(low,high)
  arr[r],arr[high]=arr[high],arr[r]
  pivot=arr[high]
  i=low-1
  for j in range(low,high):
    if arr[j]<=pivot:
      i+=1
      arr[i],arr[j]=arr[j],arr[i]
    print("Step ",k,": ",arr)
    k+=1
  arr[i+1],arr[high]=arr[high],arr[i+1]
  return i+1

arr=[3,0,1,8,7,2,5,4,9,6]
QuickSort(arr,0,len(arr)-1)
print("\nFinal solution: ",arr)

