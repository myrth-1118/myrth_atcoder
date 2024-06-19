from collections import defaultdict
N = int(input())
S = input()
Q = int(input())
node = defaultdict(str)

for i in range(97, 123):
  node[chr(i)] = chr(i)

# アルファベットの変更を記録
for _ in range(Q):
  c, d = input().split()
  
  for i in node:
    if node[i] == c:
      node[i] = d

ans = []
for i in range(N):
  ans.append(node[S[i]])

print(''.join(ans))