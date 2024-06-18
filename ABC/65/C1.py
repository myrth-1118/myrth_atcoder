N, M = map(int,input().split())
MOD = 10**9 + 7

if abs(N - M) >= 2:
  print(0)
  exit()

def fact(n):
  a = 1
  for i in range(1, n + 1):
    a = a*i % MOD
  return a

x = fact(N)
y = fact(M)
ans = x*y % MOD

if N == M :
  ans *= 2

print(ans % MOD)