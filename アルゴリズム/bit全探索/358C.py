# bit全探索
import itertools
N, M = map(int,input().split())
S = [input() for _ in range(N)]
ans = N

arr_list = itertools.product((0,1), repeat=N)
for ptn in arr_list:
  node = [0]*M
  num = 0
  for i in range(N):
    if ptn[i] == 1:
      num += 1
      for j in range(M):
        if S[i][j] == 'o':
          node[j] = 1
  if 0 not in node:
    ans = min(ans, num)

print(ans)