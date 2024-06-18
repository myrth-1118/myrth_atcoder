N, M = map(int,input().split())
L = []
R = []
for i in range(M):
  Li, Ri = map(int,input().split())
  L.append(Li)
  R.append(Ri)

Lx = max(L)
Rx = min(R)

if Rx - Lx + 1 >= 0:
  print(Rx - Lx + 1)
else:
  print(0)