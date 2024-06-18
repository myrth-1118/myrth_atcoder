# 順列全探索 組合せ重複なし 単調増加数列
import itertools
N, M = map(int,input().split())

arr_list = itertools.combinations(range(1,M + 1),N)

for i in arr_list:
  print(*i)