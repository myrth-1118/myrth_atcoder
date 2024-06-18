# 2次元DP
N, M = map(int,input().split())
A = []
mod = 10**9 + 7
num = 0

for _ in range(M):
  a = int(input())
  A.append(a)
  
A.append(0)
dp = [0]*(N + 1)
dp[0] = 1

for i in range(1,N + 1):
  dp[i] = (dp[i - 1] + dp[i - 2]) % mod
  if i == A[num]:
    dp[i] = 0
    num += 1

print(dp[N])