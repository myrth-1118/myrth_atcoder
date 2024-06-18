# bit全探索
from itertools import product
N = int(input())

for pro in product(('a','b','c'),repeat=N):
  print(''.join(pro))