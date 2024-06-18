# bit全探索
import itertools
import collections
N, K = map(int,input().split())
S = [input() for _ in range(N)]
node = []
ans = 0

arr_list = itertools.product((0,1), repeat=N)

for ptn in arr_list:
  num = 0
  node.clear()
  for i in range(N):
    if ptn[i] == 1:
      
      for j in S[i]:
        node.append(j)
        
  c = collections.Counter(node)
  for j in c.values():        # 各文字の個数を取得
    if j == K:
      num += 1
 
  ans = max(ans, num)

print(ans)