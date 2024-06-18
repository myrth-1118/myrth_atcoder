# 二分探索bisect
import bisect
N, Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

for i in range(Q):
  num = int(input())
  x = bisect.bisect_left(A,num)
  print(N - x)