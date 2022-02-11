# https://codeforces.com/problemset/problem/282/A

n = int(input())
res = 0

for i in range(n):
  arr = str(input())
  if arr[1] == '+':
    res +=1
  elif arr[1] == '-' :
    res -=1

print(res)