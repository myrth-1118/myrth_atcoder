# 順列全探索 順列重複なし
import itertools
N, M = map(int,input().split())
P = [[False]*N for _ in range(N)]
Q = [[False]*N for _ in range(N)]

for _ in range(M):
  A, B = map(int,input().split())
  P[A - 1][B - 1] = P[B - 1][A - 1] = True

for _ in range(M):
  C, D = map(int,input().split())
  Q[C - 1][D - 1] = Q[D - 1][C - 1] = True

arr_list = itertools.permutations(range(N),N)

for ptn in arr_list:
  flag = True
  for i in range(N):
    for j in range(N):
      if P[i][j] != Q[ptn[i]][ptn[j]]:
        flag = False
  if flag:
    print('Yes')
    exit()

print('No')