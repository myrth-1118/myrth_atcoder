# 累積和
from itertools import accumulate
N, M = map(int,input().split())
A = [0] + list(map(int,input().split()))
a=list(accumulate(A))
num = 0

for i in range(1,M + 1):
  num += A[i]*i
  
ans = num

for i in range(N - M):
  num = num - A[i + 1] - a[M + i] + a[i + 1] + A[M + i + 1]*M
  ans = max(ans,num)

print(ans)