N, K = map(int,input().split())
a = list(map(int,input().split()))
b = sorted(a)
c = (N - 1) % K
ans = 'Yes'

for i in range(K):
  node, check = [], []
  if i <= c:
    hani = (N - 1) // K + 1
  else:
    hani = (N - 1) // K
  
  for j in range(hani):
    node.append(a[i + j*K])
    check.append(b[i + j*K])
  
  if sorted(node) != check:
    ans = 'No'

print(ans)