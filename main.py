 # arr = [1,4,5,1,2,5,1,2,3,2,3,3,2,5,0,5,3,1,3,0]
# arr = [5,5,0,4,1,4,5,5,3,2]
# arr = [5,5,0,2,2,0,1,0,3,2]
arr = [1,3,5,8,9,2,6,7,6,8,9]
n = len(arr)
current_idx = 0
step = arr[0]
jumps = 1
while n >= 0 :
  print(jumps)
  print(arr[current_idx],current_idx,step)
  n -= step
  print('sdknv',n,step)
  if arr[current_idx] == 0 :
    jumps = -1
    break
  elif n <= 1 :
    break
  else :
    current_idx += step
    step = arr[current_idx]
    print('sdkns',step,n)
    jumps += 1

print(jumps)