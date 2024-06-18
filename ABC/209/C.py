N = int(input())
C = map(int,input().split())
num = 0
ans = 1
mod = 10**9 + 7

for i in sorted(C):
  ans *= (i - num) % mod
  ans %= mod
  num += 1

print(ans)