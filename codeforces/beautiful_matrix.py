# https://codeforces.com/problemset/problem/263/A

res = 0

for i in range(5):
  arr = list(input().split(" "))
  for j in range(5):
    if arr[j] == '1':
      # print(i,j)
      res = abs(2-i) + abs(2-j)

print(res)