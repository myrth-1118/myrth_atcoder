import math
D = int(input())
ans = D

for i in range(int(math.sqrt(D)) + 1):
  a = D - i**2
  b = int(math.sqrt(a))
  ans = min(ans,abs(a - b**2),abs(a - (b + 1)**2))

print(ans)