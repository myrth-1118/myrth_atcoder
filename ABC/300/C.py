H, W = map(int,input().split())
C = [input() for _ in range(H)]
dx = [1,1,-1,-1]
dy = [1,-1,1,-1]
ans = [0]*min(H, W)

for i in range(1,H):
  for j in range(1,W):
    x, y = i, j
    if C[x][y] == '#':
      flag = True
      dr = 1
      
      while flag:
        for k in range(4):
          nx = x + dx[k]*dr
          ny = y + dy[k]*dr
          if 0 <= nx < H and 0 <= ny < W and C[nx][ny] == '#':
            pass
          else:
            flag = False
            
        if flag:
          dr += 1
        
        else:
          if dr >= 2:
            ans[dr - 2] += 1

print(*ans)