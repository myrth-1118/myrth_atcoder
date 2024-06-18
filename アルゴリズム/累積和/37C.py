# 累積和
N, K = map(int,input().split())
a = [0] + list(map(int,input().split()))   # あとで引き算をするためa[0]に0を追加
ans = 0

for i in range(N):
  a[i + 1] += a[i]

for i in range(K,N + 1):  # 始点はK
  ans += a[i] - a[i - K]

print(ans)