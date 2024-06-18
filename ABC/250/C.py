N, Q = map(int,input().split())
ans = list(range(1, N + 1))
node = list(range(N))

for _ in range(Q):
  x = int(input())
  a = node[x - 1]
  
  if a == N - 1:   # 右端の場合
    b = node[x - 1] - 1
  else:
    b = node[x - 1] + 1
  
  y = ans[b]
  
  ans[a], ans[b] = ans[b], ans[a]
  node[x - 1], node[y - 1] = node[y - 1], node[x - 1]

print(*ans)