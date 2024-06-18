import math
N, X = map(int,input().split())
x = list(map(int,input().split()))
ans = abs(X - x[0])

for i in x:
  a = abs(X - i)
  ans = math.gcd(ans, a)

print(ans)