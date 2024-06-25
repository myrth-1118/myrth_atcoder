N, M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
k = 10**9
node = []
num = 0
ans = 0

# A[i],A[i+1]の差(スタンプを押す面積)をpに入れる
for i in A:
  p = i - num - 1
  
  if p != 0:
    node.append(p)
    k = min(k, p)
  num = i
  
# 一番右の面積を考慮する
if num != N:
  node.append(N - num)
  k = min(k, N - num)

if len(node) == 0:
  print(0)
  exit()

for i in node:
  ans += (i - 1) // k + 1

print(ans)