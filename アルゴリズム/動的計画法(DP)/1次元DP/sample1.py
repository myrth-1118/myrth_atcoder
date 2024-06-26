# DP (DPまとめコンテスト)
N = int(input())
h = list(map(int,input().split()))

dp = [0]*N   # dp[i]=i番目の足場に行くまでの最低コスト

dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2,N):
  dp[i] = min(dp[i -2] + abs(h[i] - h[i - 2]),dp[i - 1] + abs(h[i] - h[i - 1]))

print(dp[-1])