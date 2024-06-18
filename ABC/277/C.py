# 幅優先探索 グラフと頂点
from collections import defaultdict
from collections import deque
N = int(input())
node = defaultdict(list)
check = defaultdict(int)

for _ in range(N):
  A, B = map(int,input().split())
  node[A - 1].append(B - 1)
  node[B - 1].append(A - 1)
  check[A - 1], check[B - 1] = 0, 0

q = deque([0])
ans = 1

while len(q) != 0:
  now = q[0]
  q.popleft()
  
  if check[now] == 0:
    check[now] = 1
    for i in node[now]:
      if check[i] == 0:
        q.append(i)
        ans = max(ans, i + 1)

print(ans)