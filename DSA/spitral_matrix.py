# Given an integer matrix of size N x N. Traverse it in a spiral form.
## Imput
matrix = [[1,2,3],[4,5,6],[7,8,9]]
n=3
arr = []
start_idx = 0
lower_limit_row = start_idx
upper_limit_row = n
lower_limit_col = start_idx
upper_limit_col = n
while(lower_limit_col < upper_limit_col and lower_limit_row < upper_limit_row):
  for j in range(lower_limit_row,upper_limit_row):
    arr.append(matrix[lower_limit_row][j])
  lower_limit_col +=1
  for j in range(lower_limit_col,upper_limit_col):
    arr.append(matrix[j][upper_limit_col-1])
  upper_limit_row -=1
  print("1st")
  print(lower_limit_col)
  print(upper_limit_col)
  print(lower_limit_row)
  print(upper_limit_row)
  if lower_limit_col < upper_limit_col :
    for j in range(upper_limit_row-1,lower_limit_row-1,-1):
      arr.append(matrix[upper_limit_row][j])
    upper_limit_col -=1
  print("2nd")
  print(lower_limit_col)
  print(upper_limit_col)
  print(lower_limit_row)
  print(upper_limit_row)
  if lower_limit_col < upper_limit_col :
    for j in range(upper_limit_col-1,lower_limit_col-1,-1):
      arr.append(matrix[j][lower_limit_col-1])
    lower_limit_row +=1
  print("3rd")
  print(lower_limit_col)
  print(upper_limit_col)
  print(lower_limit_row)
  print(upper_limit_row)
print(arr)