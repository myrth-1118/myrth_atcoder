# 二分探索bisect
import bisect
N = int(input())
start = []
check = []
ans = 0

for i in range(N):
  l, r = map(int,input().split())
  start.append(l)
  check.append((l,r))

A = sorted(start)
B = sorted(check)

for i in range(N - 1):
  ans += bisect.bisect_right(A,B[i][1]) - i - 1
  
print(ans)