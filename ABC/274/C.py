# 幅優先探索 グラフと頂点
from collections import deque
N = int(input())
A = list(map(int,input().split()))
node = [[] for i in range(2*N + 2)]   # 分かりやすいように0スタート(出力は1からにする)
dist = [0 for i in range(2*N + 2) ]   # 距離順のリスト

for i in range(N):                   # 上(1)から下へ行く一方通行のnodeの作成
  node[A[i]].append(2*(i + 1))
  node[A[i]].append(2*(i + 1) + 1)


q = deque([1])    # 最初にqには頂点(1)の座標のみを入れる

for i in node[1]: # 頂点1と繋がっているものを距離1にする
  dist[i] = 1

while len(q) != 0:
  now = q[0]
  q.popleft()
  for i in node[now]:        # 各頂点の1からの距離をdistに記録
    dist[i] = dist[now] + 1
    q.append(i)

for i in range(1,2*N + 2):
  print(dist[i])