from collections import defaultdict
N = int(input())
p = list(map(int,input().split()))
node = defaultdict(int)
ans = 0

for i in range(N):
  if p[i] == i:
    node[0] += 1
    node[1] += 1
    node[N - 1] += 1
  
  elif p[i] > i:
    node[p[i] - i] += 1
    node[(p[i] - i + 1) % N] += 1
    node[(p[i] - i - 1) % N] += 1
  
  else:
    node[N - i + p[i]] += 1
    node[(N - i + p[i] + 1) % N] += 1
    node[(N - i + p[i] - 1) % N] += 1

for i in node:
  ans = max(ans,node[i])

print(ans)