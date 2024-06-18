# 二分探索bisect
import bisect
N, M = map(int,input().split())
A = list(map(int,input().split()))
ans = 0

a = sorted(A)

for i in range(N):
  left = bisect.bisect_left(a,a[i])
  right = bisect.bisect_left(a,a[i] + M)
  ans = max(ans,right - left)

print(ans)