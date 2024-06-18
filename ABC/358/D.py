# 優先度付きキュー
import heapq
from collections import defaultdict
N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
B.sort()
mx = []
ans = 0

for i in A:
  heapq.heappush(mx, i)

for i in B:
  while len(mx) != 0 and mx[0] < i:
    heapq.heappop(mx)
  if len(mx) == 0:
    print(-1)
    exit()
  else:
    ans += mx[0]
    heapq.heappop(mx)

print(ans)