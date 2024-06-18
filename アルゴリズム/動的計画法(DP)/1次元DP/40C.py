# 1次元DP
N = int(input())
a = list(map(int,input().split()))

dp = [0]*N    # dp[i]= i番目の足場に行くまでの最低コスト
dp[0] = 0
dp[1] = abs(a[1] - a[0])

for i in range(2,N): # xとyで小さい方を取得
  x = abs(a[i] - a[i - 2])
  y = abs(a[i] - a[i - 1])
  dp[i] = min(dp[i - 2] + x,dp[i - 1] + y)

print(dp[-1])