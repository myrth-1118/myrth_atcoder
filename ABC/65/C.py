import math
N, M = map(int,input().split())
MOD = 10**9 + 7

if abs(N - M) >= 2:
  print(0)
  exit()

a = math.factorial(N) % MOD
b = math.factorial(M) % MOD

ans = a*b % MOD

if N == M :
  ans *= 2

print(ans % MOD)