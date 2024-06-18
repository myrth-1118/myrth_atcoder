N, M = map(int,input().split())
node = []

for i in range(M):
  a, b = map(int,input().split())
  if a == 1:
    node.append(b)
  if b == N:
    node.append(a)

if len(node) != len(set(node)):
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')