# 二分探索bisect
# 累積和
import bisect
N, M, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A_count = [0]*(N + 1)
B_count = [0]*(M + 1)
ans = 0

for i in range(N):
  A_count[i + 1] = A_count[i] + A[i]

for i in range(M):
  B_count[i + 1] = B_count[i] + B[i]

for i in range(N + 1):
  if A_count[i] <= K:
    x = bisect.bisect_right(B_count,K - A_count[i])
    ans = max(ans,x - 1 + i)
  else:
    break
  
print(ans)