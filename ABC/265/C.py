H, W = map(int,input().split())
G = [input() for i in range(H)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
x = 0
y = 0
nx = 0
ny = 0

for i in range(300000):
  if G[x][y] == 'R' and 0 <= x + dx[0] < H and 0 <= y + dy[0] < W:
    nx = x + dx[0]
    ny = y + dy[0]
  if G[x][y] == 'L' and 0 <= x + dx[1] < H and 0 <= y + dy[1] < W:
    nx = x + dx[1]
    ny = y + dy[1]
  if G[x][y] == 'D' and 0 <= x + dx[2] < H and 0 <= y + dy[2] < W:
    nx = x + dx[2]
    ny = y + dy[2]
  if G[x][y] == 'U' and 0 <= x + dx[3] < H and 0 <= y + dy[3] < W:
    nx = x + dx[3]
    ny = y + dy[3]
    
  if nx == x and ny == y:
    print(x + 1,y + 1)
    exit()
  
  x, y = nx, ny

print(-1)