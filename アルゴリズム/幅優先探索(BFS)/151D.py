# 幅優先探索 迷路
from collections import deque
H, W = map(int,input().split())
S = [list(input()) for i in range(H)]
ans = 0
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

for i in range(H):  # スタート地点
  for j in range(W):
    dist = [[-1]*W for i in range(H)]    # distを入力する場所
    if S[i][j] == '.':
      dist[i][j] = 0      # スタート地点を0に設定
      q = deque()
      q.append((i,j))
      check(i,j)          # check()を実行
      
      num = 0
      num_max = 0
      
      for k in range(H):  # ゴール地点
        for l in range(W):
          num = dist[k][l]            # ゴール地点までの最短距離
          num_max = max(num_max,num)  # スタート地点から最も遠い所の距離
      
      ans = max(ans,num_max)

print(ans)