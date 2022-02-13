# https://codeforces.com/contest/514/problem/A

num = str(input())
result = str()
count = 0

for n in num : 
  n = int(n)
  if count == 0 and n == 9 :
    pass
  elif n >= 5 :
    n = 9-n
  result = result + str(n)
  count +=1

print(int(result))

