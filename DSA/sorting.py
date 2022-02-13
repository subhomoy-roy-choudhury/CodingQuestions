# Best case :- O(n)
# Average case :- O(n^2)
# Worst Case :- O(n^2)
# Space Complexity :- O(1)
def bubble_sort(arr):
  for i in range(len(arr)) :
    for j in range(i,len(arr)):
      if arr[i] > arr[j]:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
  return arr

# Best case :- O(n^2)
# Average case :- O(n^2)
# Worst Case :- O(n^2)
# Space Complexity :- O(1)
def selection_sort(arr):
  for i in range(len(arr)):
    max_num = i
    for j in range(i,len(arr)):
      if arr[max_num] < arr[j]:
        max_num = j
    arr[i],arr[max_num] = arr[max_num],arr[i]
  return arr

# Best case :- O(n^2)
# Average case :- O(n^2)
# Worst Case :- O(n^2)
# Space Complexity :- O(1)
def insertion_sort(arr):
  for i in range(1,len(arr)):
    key = arr[i]
    j = i-1
    while j>=0 and key < arr[j]:
      arr[j+1] = arr[j]
      j-=1
    arr[j+1] = key
  return arr 

# Best case :- O(nlogn)
# Average case :- O(nlogn)
# Worst Case :- O(nlogn)
# Space Complexity :- O(1)
class HeapSort:
  def __init__(self,arr):
    n=len(arr)
    for i in range(n//2,-1,-1):
      self.heapify(arr,n,i)
    for i in range(n-1,0,-1):
      arr[i],arr[0] = arr[0],arr[i]
      self.heapify(arr,i,0)

  def heapify(self,arr,n,i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[i] < arr[left] :
      largest = left
    
    if right < n and arr[largest] < arr[right] :
      largest = right

    if largest != i:
      arr[largest],arr[i] = arr[i],arr[largest]
      self.heapify(arr,n,largest) 

# Best case :- O(nlogn)
# Average case :- O(nlogn)
# Worst Case :- O(nlogn)
# Space Complexity :- O(n)
def merge_sort(arr):
  if len(arr)>1:
    mid = len(arr)//2 
    L = arr[:mid]
    R= arr[mid:]

    merge_sort(L)
    merge_sort(R)

    i=j=k=0
    while i<len(L) and j<len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i+=1
      else :
        arr[k] = R[j]
        j+=1
      k+=1
    
    while i<len(L):
      arr[k] = L[i]
      i+=1
      k+=1
    
    while j < len(R) :
      arr[k] = R[j]
      j+=1
      k+=1

# Best case :- O(nlogn)
# Average case :- O(nlogn)
# Worst Case :- O(n62)
# Space Complexity :- O(logn)
class QuickSort:
  def __init__(self,arr):
    size = len(arr)
    self.quick_sort(arr,0,size-1)
  
  def partition(self,arr,low,high):

    i = low -1
    pivot = arr[high]
    for j in range(low,high):
      if arr[j] <= pivot:
        i+=1
        arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1


  def quick_sort(self,arr,low,high):
    if low<high :
      pivot = self.partition(arr,low,high)

      self.quick_sort(arr,low,pivot-1)
      self.quick_sort(arr,pivot+1,high)
  

if __name__ == '__main__':

  arr = [1,3,2,6,5,4]
  print(f'Bubble Sort --> {bubble_sort(arr)}')
  arr = [1,3,2,6,5,4]
  print(f'Selection Sort --> {selection_sort(arr)}')
  arr = [1,3,2,6,5,4]
  print(f'Insertion Sort --> {insertion_sort(arr)}')
  arr = [1,3,2,6,5,4]
  HeapSort(arr)
  print(f'Heap Sort --> {arr}')
  arr = [1,3,2,6,5,4]
  merge_sort(arr)
  print(f'Merge Sort --> {arr}')
  arr = [1,3,2,6,5,4]
  QuickSort(arr)
  print(f'Quick Sort --> {arr}')