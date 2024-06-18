# 2次元DP
N = int(input())
check = []
dp = [0]*300
dp[0] = 1
dp[1] = 1
dp[2] = 1

for i in range(3):
  NG = int(input())
  check.append(NG)
  dp[NG - 1] = 1000

for i in range(3,N):
  dp[i] = min(dp[i - 1],dp[i - 2],dp[i - 3]) + 1
  if i + 1 in check:
    dp[i] = 1000

if dp[N - 1] <= 100:
  print('YES')
else:
  print('NO')