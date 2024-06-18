from collections import defaultdict
n = int(input())
S = [input() for i in range(n)]
node = defaultdict(int)
ans = []

for i in range(len(S[0])):
  node[S[0][i]] += 1

for i in range(1, n):
  check = defaultdict(int)
  for j in range(len(S[i])):
    check[S[i][j]] += 1
  
  for k in node:
    if node[k] > check[k]:
      node[k] = check[k]

for i in sorted(node):
  if node[i] != 0:
    for j in range(node[i]):
      ans.append(i)

print(''.join(ans))