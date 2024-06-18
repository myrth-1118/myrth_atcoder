# 幅優先探索 迷路
from collections import deque
H, W = map(int,input().split())
S = [list(input()) for i in range(H)]
a = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
dist = [[-1]*W for i in range(H)]    # distを入力する場所

def check(cx,cy):
  while len(q) != 0:    # 全て終わったら0になる
    cx,cy = q[0]
    q.popleft()
    for i in range(4):
      px = cx + dx[i]
      py = cy + dy[i]
      
      if 0 <= px < H and 0 <= py < W and S[px][py] == '.' and dist[px][py] == -1:
        dist[px][py] = dist[cx][cy] + 1
        q.append((px,py))

for i in range(H):
  for j in range(W):
    if S[i][j] == '.':
      a += 1          # '.'の数をカウント

dist = [[-1]*W for i in range(H)]    # distを入力する場所

dist[0][0] = 0      # スタート地点を0に設定
q = deque()
q.append((0,0))
check(0,0)          # check()を実行
      
num = dist[H - 1][W - 1]  # ゴール地点までの最短距離
ans = a - num - 1

if num == -1:
  print(-1)
else:
  print(ans)