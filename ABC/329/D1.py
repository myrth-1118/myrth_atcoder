from collections import defaultdict
N, M = map(int,input().split())
A = list(map(int,input().split()))
node = defaultdict(int)

node[A[0] - 1] += 1
print(A[0])
mx = A[0] - 1

for i in range(1, M):
  p = A[i] - 1
  node[p] += 1
  
  # 最大値mxとpの比較
  if node[mx] > node[p]:
    print(mx + 1)
  elif node[mx] < node[p]:
    print(p + 1)
    mx = p
  else:
    mx = min(mx, p)
    print(mx + 1)