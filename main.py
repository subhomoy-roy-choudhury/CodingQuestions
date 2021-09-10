
def bubble_sort(arr):
  for i in range(len(arr)) :
    for j in range(i,len(arr)):
      if arr[i] > arr[j]:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
  return arr

def selection_sort(arr):
  

if __name__ == '__main__':

  arr = [1,3,2,6,5,4]
  print(f'Bubble Sort --> {bubble_sort(arr)}')

