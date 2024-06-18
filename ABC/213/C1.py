from collections import defaultdict
H, W, N = map(int,input().split())
tate, yoko = defaultdict(int), defaultdict(int)
tate1, yoko1 = [], []
node = []

for i in range(N):
  A, B = map(int,input().split())
  node.append((A, B))
  tate1.append(A)
  yoko1.append(B)

num = 1
for i in sorted(set(tate1)):
  tate[i] = num
  num += 1

num = 1
for i in sorted(set(yoko1)):
  yoko[i] = num
  num += 1

for x, y in node:
  print(tate[x], yoko[y])