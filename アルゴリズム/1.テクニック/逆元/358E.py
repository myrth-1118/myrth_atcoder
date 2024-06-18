K = int(input())
C = list(map(int,input().split()))
MOD = 998244353
n = 26

# 階乗の計算
fact = [1]*(K + 1)
for i in range(1, K + 1):
  fact[i] = fact[i - 1]*i % MOD
  
# 階乗の逆元の計算
ifact = [1]*(K + 1)
ifact[K] = pow(fact[K], MOD - 2, MOD)
for i in range(K, 0, -1):
  ifact[i - 1] = ifact[i]*i % MOD

def comb(n, r):
  if r > n or r < 0:
    return 0
  return fact[n]*ifact[r] % MOD * ifact[n - r] % MOD

dp = [[0]*(K + 1) for _ in range(n + 1)]
dp[0][0] = 1

# 使用した文字の種類数
for i in range(n):
  # 今までに使用した文字の数
  for j in range(K + 1):
    # これから使用する文字の数
    for a in range(C[i] + 1):
      nj = j + a
      if nj > K:
        break
      # 組合せの計算
      dp[i + 1][nj] += dp[i][j] * comb(nj, a) % MOD
      dp[i + 1][nj] %= MOD

ans = 0
for i in range(1, K + 1):
  ans += dp[-1][i]
  ans %= MOD

print(ans)