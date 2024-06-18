N = int(input())
num = 0
L = []

for _ in range(N):
  A, B = map(int,input().split())
  L.append((A, B))
  num += A / B

check = num / 2
num = 0
length = 0

for a, b in L:
  num += a / b
  
  if num < check:
    length += a
    continue
  
  else:
    length += (check - num + a / b)*b
    print(length)
    exit()