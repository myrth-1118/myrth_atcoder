# 約数列挙・判定
N, M = map(int,input().split())
ans = 0

def divide(x):
  i = 1
  lower, upper = [],[]
  while i*i <= x:
    if x % i == 0:
      lower.append(i)
      if x // i != i:
        upper.append(x // i)
    i += 1
  return lower + upper[::-1]
  
D = divide(M)
for i in D:
  if M // i >= N:
    ans = i

print(ans)