# bitDP
from collections import defaultdict
N, K = map(int,input().split())
S = list(input())
MOD = 998244353

dp = [defaultdict(int) for _ in range(N + 1)]
dp[0][''] = 1

# 文字列k+cが回文であるかの確認
def p(n):
  return len(n) == K and n == n[::-1]

for i in range(N):
  # kが現在の状態、vがその状態になる数
  for k, v in dp[i].items():
    # AとBのそれぞれについて調べる
    for c in 'AB':
      # 文字列k+cが回文でないとき
      if S[i] in [c, '?'] and not p(k + c):
        # 文字列k+cの後ろからK - 1をnkとする
        nk = (k + c)[-(K - 1) :]
        # dp[i][k]の値がvであるため、既にある値にvを加算
        dp[i + 1][nk] = (dp[i + 1][nk] + v) % MOD

print(sum(dp[N].values()) % MOD)