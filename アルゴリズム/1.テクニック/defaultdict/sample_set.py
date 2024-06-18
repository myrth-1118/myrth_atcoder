# ABC278C
from collections import defaultdict
N, Q = map(int,input().split())
node = defaultdict(set)

for i in range(Q):
  T, A, B = map(int,input().split())
  
  if T == 1:
    node[A].add(B)      # set型に追加するときはappendではなくadd
  
  elif T == 2:
    node[A].discard(B)  # removeだと要素がないときにエラーとなるためdiscard
  
  else:
    if B in node[A] and A in node[B]:
      print('Yes')
    else:
      print('No')