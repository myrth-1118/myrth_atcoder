# 幅優先探索 グラフと頂点
from collections import deque
N, X, Y = map(int,input().split())
node = [[] for i in range(N)]
Map = [[] for i in range(N)]     # 最短距離順に並び替えたリスト
ans = []

for i in range(N - 1):
  A, B = map(int,input().split())
  A -= 1
  B -= 1
  node[A].append(B)               # nodeに保管
  node[B].append(A)
inf = 10**9
dist = [inf for i in range(N)]

dist[Y - 1] = 0     # ゴール地点Y-1を距離0,基準に設定
Map[dist[Y - 1]] = [Y - 1]
q = deque([Y - 1])  # deque()に保管

while len(q) != 0:
  now = q[0]
  q.popleft()
  for i in node[now]:           # 最初はnode[0]から引き出す
    if dist[i] > dist[now] + 1:
      dist[i] = dist[now] + 1
      Map[dist[i]].append(i)
      q.append(i)
      
num_start = dist[X - 1]
ans.append(X)
num = X - 1

while num != Y - 1:   # スタートから初めてゴールにたどり着いたら終了
  for i in node[num]:
    if i in Map[dist[num] - 1]:
      ans.append(i + 1)
      num = i

print(*ans)