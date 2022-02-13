#Q [3,2,5,1,9]  ---> [3,5,9] 
a = [3,2,5,1,9]
i = 0
while(a[i] is not None):
  flag = 0
  if len(a) == 1:
    print(a)
    break
  print(a)
  print(a[i],a[i+1])
  if a[i] > a[i+1]:
    a.pop(i+1)
    print(a)
    flag +=1
  print(i)
  i+=1
  print(len(a)) 
  if flag == 0 and i == len(a)-1 :
    break 
  elif flag == 1 :
    i = 0
print(a)