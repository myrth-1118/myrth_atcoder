# 幅優先探索 グラフと頂点
from collections import deque
N, M = map(int,input().split())
node = [[] for i in range(N)]  
for i in range(M):
  A, B = map(int,input().split())
  A -= 1
  B -= 1
  node[A].append(B)
  node[B].append(A)

inf = 10**9
dist = [inf for i in range(N)]
num = 0
ans = 'No'

def check(x):
  dist[x] = 0
  q = deque([x])  # deque()に保管
  while len(q) != 0:
    now = q[0]
    q.popleft()
    for i in node[now]:           # 最初はnode[0]から引き出す
      if dist[i] > dist[now] + 1:
        dist[i] = dist[now] + 1
        q.append(i)

check(0)
P = []
for i in range(N):
  P.append(len(node[i]))

num_max = max(P)
num_min = min(P)
  
if N == 2:
  if M == 1:
    ans = 'Yes'
else:
  if num_max == 2 and num_min == 1 and M == N - 1 and 10**9 not in dist:
    ans = 'Yes'

print(ans)