# 2次元DP
N = int(input())
dp = [[0]*9 for _ in range(N)]
ans = 0
mod = 998244353

for i in range(9):
  dp[0][i] = 1

for i in range(1,N):
  for j in range(9):
    if j == 0:
      dp[i][j] = (dp[i - 1][j] + dp[i - 1][j + 1]) % mod
    elif j == 8:
      dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % mod
    else:
      dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod

for i in range(9):
  ans += dp[-1][i] % mod

print(ans % mod)