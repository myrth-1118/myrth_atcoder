N = int(input())
num = 0

for i in range(1,N + 1):
  flag = True
  a = str(i)
  for j in range(len(a)):
    if a[j] == '7':
      flag = False
  
  S = oct(i)
  b = str(S)
  for k in range(len(b)):
    if b[k] == '7':
      flag = False
  
  if flag == True:
    num += 1

print(num)