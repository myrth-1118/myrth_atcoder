# 幅優先探索 グラフと頂点
from collections import deque
N, M = map(int,input().split())
node = [[] for i in range(N)]  

for i in range(M):
  A, B = map(int,input().split())
  A -= 1
  B -= 1
  node[A].append(B)               # nodeに保管
  node[B].append(A)

inf = 10**9
dist = [inf for i in range(N)]
num = 0

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

for i in range(N):   # 探索が終わってない所をcheck()する
  if dist[i] == 10**9:
    check(i)
    num += 1
  else:
    continue
  
print(num)