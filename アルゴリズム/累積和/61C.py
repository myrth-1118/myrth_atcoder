# 累積和
N, K = map(int,input().split())
P = []
for i in range(N):
  a, b = map(int,input().split())
  P.append((a,b))

P.sort()
num = 0

for a, b in P:
  if num + b < K:
    num += b
  else:
    ans = a
    break

print(ans)