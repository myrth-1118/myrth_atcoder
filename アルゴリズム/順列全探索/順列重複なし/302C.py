# 順列全探索 順列重複なし
import itertools
N, M = map(int,input().split())
S = [input() for _ in range(N)]

arr_list = itertools.permutations(range(N),N)

for ptn in arr_list:
  flag = True
  for i in range(N - 1):
    num = 0
    for j in range(M):
      if S[ptn[i]][j] != S[ptn[i + 1]][j]:
        num += 1
    if num >= 2:
      flag = False
  
  if flag:
    print('Yes')
    exit()

print('No')