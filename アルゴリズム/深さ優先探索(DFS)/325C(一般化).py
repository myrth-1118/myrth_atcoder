# 深さ優先探索
import sys
sys.setrecursionlimit(10**9) # 再帰回数の上限設定
H, W = map(int,input().split())
S = [list(input()) for i in range(H)]
dx = [1,1,1,-1,-1,-1,0,0]
dy = [1,0,-1,1,0,-1,1,-1]
ans = 0     # センサーの数

def dfs(x,y):
  if S[x][y] == '#':
    S[x][y] = '.'
    
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '#':
      dfs(nx,ny)
  
  return  # for文が全て終わったとき終了

for i in range(H):
  for j in range(W):
    if S[i][j] == '#':
      dfs(i,j)
      ans += 1   # センサーの数をカウント
    
    else:
      continue

print(ans)