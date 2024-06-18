N = int(input())
a = 1
ans = N
check = []

for i in range(2,10**6):
  if i**2 > N:
    break
  else:
    num = 2
    while i**num <= N:
      check.append(i**num)
      num += 1
    
print(ans - len(set(check)))