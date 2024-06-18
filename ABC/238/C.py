N = int(input())
S = str(N)
a = len(S)
MOD = 998244353
ans = 0
n = 1

for _ in range(a - 1):
  ans += (9*n*(9*n + 1) // 2) % MOD
  n *= 10

x = N - 10**(a - 1) + 1
ans += (x*(x + 1) // 2) % MOD

print(ans % MOD)