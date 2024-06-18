# 幅優先探索 迷路
from collections import deque
R, C = map(int,input().split())
sy, sx = map(int,input().split())
gy, gx = map(int,input().split())
c = [list(input()) for i in range(R)]
sy -= 1
sx -= 1
gy -= 1
gx -= 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
dist = [[10000]*C for i in range(R)]    # distを入力する場所

dist[sy][sx] = 0      # スタート地点を0に設定
q = deque()
q.append((sx,sy))

while len(q) != 0:    # 全て終わったら0になる
  cx,cy = q[0]
  q.popleft()
  for i in range(4):
    px = cx + dx[i]
    py = cy + dy[i]
    
    if 0 <= py < R and 0 <= px < C and c[py][px] == '.':
      if dist[py][px] > dist[cy][cx] + 1:
        dist[py][px] = dist[cy][cx] + 1
        q.append((px,py))

print(dist[gy][gx])