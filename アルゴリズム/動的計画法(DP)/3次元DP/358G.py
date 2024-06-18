# 3次元DP
H, W, K = map(int,input().split())
Si, Sj = map(int,input().split())
Si -= 1
Sj -= 1
A = [list(map(int,input().split())) for _ in range(H)]
INF = -10**18
ans = 0
a = min(K, H*W)

dp = [[[INF]*W for _ in range(H)] for _ in range(a + 1)]
dp[0][Si][Sj] = 0                                            # 一番左には移動回数を入れる

for t in range(a): # 移動回数
  for i in range(H):
    for j in range(W):
      
      ans = max(ans, dp[t][i][j] + A[i][j]*(K - t)) # (i,j)で移動しない場合
      
      for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        ni, nj = i + di, j + dj
        
        if 0 <= ni < H and 0 <= nj < W:
          if t != 0:
            dp[t + 1][ni][nj] = max(dp[t + 1][ni][nj], dp[t][i][j] + A[ni][nj], dp[t][ni][nj] + A[ni][nj])
          else:
            if abs(Si - ni) + abs(Sj - nj) <= 1:
              dp[t + 1][ni][nj] = max(dp[t + 1][ni][nj], A[ni][nj])

print(ans)