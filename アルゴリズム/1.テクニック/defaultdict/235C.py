from collections import defaultdict
N, Q = map(int,input().split())
a = list(map(int,input().split()))
num = defaultdict(list)

for i in range(N):
  num[a[i]] += [i + 1]

for _ in range(Q):
  x, k = map(int,input().split())
  if num[x] != 0 and len(num[x]) >= k:
    print(num[x][k - 1])
  else:
    print(-1)