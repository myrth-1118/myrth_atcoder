# DP
from collections import defaultdict
N, X = map(int,input().split())
node = defaultdict(int)
a1, b1 = map(int,input().split())
node[a1] = 1
node[b1] = 1
num = []
num_pop = []

for _ in range(N - 1):
  a, b = map(int,input().split())
  num.clear()
  num_pop.clear()
  
  for i in node:
    if node[i] == 1:
      num.append(a + i)
      num.append(b + i)
      num_pop.append(i)

  for i in num_pop:
    node[i] = 0
  for i in num:
    node[i] = 1

if node[X] == 1:
  print('Yes')
else:
  print('No')