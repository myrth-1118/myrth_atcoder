from collections import defaultdict
N = int(input())
a = list(map(int,input().split()))
node = defaultdict(int)
ans = 0

for i in a:
  node[i] += 1

for i in node:
  if node[i] > i:
    ans += node[i] - i
  elif node[i] < i:
    ans += node[i]

print(ans)