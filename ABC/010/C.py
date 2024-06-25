import math
tx1, ty1, tx2, ty2, T, V = map(int,input().split())
n = int(input())

for i in range(n):
  x, y = map(int,input().split())
  
  if math.sqrt((x - tx1)**2 + (y - ty1)**2) + math.sqrt((x - tx2)**2 + (y - ty2)**2) <= T*V:
    print('YES')
    exit()

print('NO')