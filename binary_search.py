arr = [1,2,3,6,9,15,22]
key = 3

# Binary Search

high_idx = len(arr)
low_idx = 0

# Brute Force Method
def binary_search_bruteforce(arr,high_idx,low_idx,key):
  print("Brute Force Method")
  while(low_idx<high_idx):
    mid_idx = (high_idx+low_idx)//2
    print(arr[mid_idx])
    if arr[mid_idx] == key :
      print("Key Found !!!!!")
      break
    elif arr[mid_idx] < key :
      low_idx = mid_idx 
    elif arr[mid_idx] > key :
      high_idx = mid_idx +1

binary_search_bruteforce(arr,high_idx,low_idx,key)

# Recursion Method 
def binary_search(key,arr):
  low_idx = 0
  high_idx = len(arr)
  mid_idx = (high_idx+low_idx)//2
  if arr[mid_idx] == key :
    print("Key Found !!!!!")
    return 0
  elif arr[mid_idx] < key :
    binary_search(key,arr[mid_idx:high_idx]) 
  elif arr[mid_idx] > key :
    binary_search(key,arr[low_idx:mid_idx+1]) 

binary_search(key,arr)