# 3次元DP
N, A = map(int,input().split())
X = list(map(int,input().split()))
ans = 0
s = sum(X)

dp = [[[0]*2501 for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0][0] = 1

for i in range(1,N + 1):
  for j in range(i):
    for k in range(2501):
      dp[i][j][k] += dp[i - 1][j][k]
      if k + X[i - 1] <= 2500:
        dp[i][j + 1][k + X[i - 1]] += dp[i - 1][j][k]


for j in range(N):
  for k in range(2501):
    if dp[-1][j][k] != 0:
      if A*(N - j) == (s - k):
        ans += dp[-1][j][k]

print(ans)