from collections import defaultdict
N = int(input())
p = list(map(int,input().split()))
node = defaultdict(int)
ans = 0

for i in range(N):
  node[(p[i] - i) % N] += 1
  node[(p[i] - i + 1) % N] += 1
  node[(p[i] - i - 1) % N] += 1
  
for i in node:
  ans = max(ans,node[i])

print(ans)