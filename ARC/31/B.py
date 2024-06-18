import copy
import sys
sys.setrecursionlimit(10**9)   # 再帰回数の上限設定
Map = [list(input()) for i in range(10)] # 'x'→海 'o'→陸
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):  # 深さ優先探索
  if New_Map[x][y] == 'o':
    New_Map[x][y] = 'x'
  
  for i in range(4):
    nx = x + dx[i]  # 移動先の座標
    ny = y + dy[i]
    if 0 <= nx < 10 and 0 <= ny < 10 and New_Map[nx][ny] == 'o':
      dfs(nx,ny)    # if文を満たすとき移動先の座標で繰り返す
      
  return  # for文が全て終わったとき終了

for i in range(10):   # 始点の位置
  for j in range(10):
    flag = True
    if Map[i][j] == 'x':    # 海のとき座標を渡す
      New_Map = copy.deepcopy(Map)
      dfs(i,j)
    else:      # elseを設定しないとREする
      continue
    for k in range(10): # 全て海かどうかの判断
      for l in range(10):
        if New_Map[k][l] == 'o':
          flag = False
    
    if flag:
      print('YES')
      exit()
      
else:
  print('NO')