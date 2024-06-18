# 約数列挙・判定
N = int(input())
node = [0]*(N - 1)
ans = 0

for k in range(1,N):
  a, b = k, N - k
    
  if node[a - 1] == 0:
    num = 0
    for i in range(1,10**3):
      if i**2 < a:
        if a % i == 0:
          num += 2
      elif i**2 == a:
        num += 1
      else:                   # aの約数の数が確定
        node[a - 1] = num
        break
  
  if node[b - 1] == 0:
    num = 0
    for i in range(1,10**3):
      if i**2 < b:
        if b % i == 0:
           num += 2
      elif i**2 == b:
        num += 1
      else:                   # bの約数の数が確定
        node[b - 1] = num
        break
  
  ans += node[a - 1]*node[b - 1]

print(ans)