# 累積和 いもす法
n = int(input())
node = [0]*1000002
ans = 0

for i in range(n):
  a, b = map(int,input().split())
  node[a] += 1
  node[b + 1] -= 1

for i in range(1000001):
  node[i + 1] += node[i]
  if ans < node[i]:
    ans = node[i]

print(ans)