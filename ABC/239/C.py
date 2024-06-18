x1, y1, x2, y2 = map(int,input().split())
dx = [2,2,1,1,-1,-1,-2,-2]
dy = [1,-1,2,-2,2,-2,1,-1]

for i in range(8):
  nx = x1 + dx[i]
  ny = y1 + dy[i]
  
  for j in range(8):
    n_nx = nx + dx[j]
    n_ny = ny + dy[j]
    
    if n_nx == x2 and n_ny == y2:
      print('Yes')
      exit()

print('No')