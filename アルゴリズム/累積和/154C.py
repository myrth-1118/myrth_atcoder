# 累積和(区間和)
N, K = map(int,input().split())
p = list(map(int,input().split()))
node = [0]

for i in range(N):
    p[i] = (p[i] + 1) / 2

for i in range(N):
  node.append(node[-1] + p[i])

ans = node[K]
for i in range(1, N - K + 1):
  num = node[K + i] - node[i]
  ans = max(ans, num)

print(ans)