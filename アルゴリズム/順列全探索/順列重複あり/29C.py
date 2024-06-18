# 順列全探索 順列重複あり
from itertools import product
N = int(input())

for pro in product(('a','b','c'),repeat=N):
  print(''.join(pro))