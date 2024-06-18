# bit全探索
import itertools
K = int(input())
ans = []

arr_list = itertools.product((0,1), repeat=10)
for ptn in arr_list:
  node = []
  for i in range(10):
    if ptn[i] == 1:
      node.append(str(i))
  a = ''.join(sorted(node,reverse=True))
  
  if a: # aが空でないとき
    ans.append(int(a))
  
ans.sort()

print(ans[K])