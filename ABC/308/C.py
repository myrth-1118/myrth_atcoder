N = int(input())
node, ans = [], []

for i in range(N):
  A, B = map(int,input().split())
  x = B*10**100 // (A + B)
  node.append((x, i + 1))

node.sort()
for x, i in node:
  ans.append(i)

print(*ans)