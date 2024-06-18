N, M = map(int,input().split())
node = []
num = 0
ans = 0

for _ in range(N):
  A, B = list(map(int,input().split()))
  node.append((A, B))

for a, b in sorted(node):
  if num + b < M:
    num += b
    ans += a*b
  else:
    ans += (M - num)*a
    print(ans)
    exit()