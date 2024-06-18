# bit全探索
import itertools
import copy
H, W, K = map(int,input().split())
c = [list(input()) for _ in range(H)]
ans = 0

arr_list = itertools.product((0,1), repeat=H)
for ptn in arr_list:
  node = copy.deepcopy(c)
  for i in range(H):
    if ptn[i] == 1:
      for j in range(W):
        node[i][j] = '.'
  
  arr1_list = itertools.product((0,1), repeat=W)
  for ptn1 in arr1_list:
    new_node = copy.deepcopy(node)
    for k in range(W):
      if ptn1[k] == 1:
        for l in range(H):
          new_node[l][k] = '.'
          
    num = 0
    for i in range(H):
      for j in range(W):
        if new_node[i][j] == '#':
          num += 1
          
    if num == K:
      ans += 1

print(ans)