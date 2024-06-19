# 2次元DP
N, M, K = map(int,input().split())
MOD = 998244353
node = [[0]*(K + 1) for _ in range(N)]
ans = 0

for i in range(1,M + 1):
  if i <= K:
    node[0][i] = 1

# node[i][j] i番目までの数字、合計がj
for i in range(N - 1):
  for j in range(K + 1):
    for k in range(1, M + 1):
      if j + k <= K:
        node[i + 1][j + k] += node[i][j] % MOD

for i in range(1, K + 1):
  ans += node[-1][i] % MOD

print(ans % MOD)