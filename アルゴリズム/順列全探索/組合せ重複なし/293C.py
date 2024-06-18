# 順列全探索 組合せ重複なし 単調増加数列
import itertools
H, W = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
ans = 0

arr_list = itertools.combinations(range(1, W + H - 1), H - 1)

for ptn in arr_list:
  x, y = 0, 0
  node = [A[0][0]]
  
  for i in range(1, W + H - 1):
    if i in ptn:
      y += 1
    else:
      x += 1
    node.append(A[y][x])
    
  if len(set(node)) == W + H - 1:
    ans += 1

print(ans)