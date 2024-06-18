# 二分探索bisect
import bisect
N, K, X = map(int,input().split())
A = list(map(int,input().split()))
node = []
node1 = []

for i in A:
  node.append(i // X)
  node1.append(i % X)

node_sort = sorted(node)   # reverseは×
node1_sort = sorted(node1,reverse=True)

B = bisect.bisect_left(node_sort,1)

if sum(node_sort[B:]) >= K:
  ans = sum(A) - K*X
  
else:
  C = K - sum(node_sort[B:])
  C_sum = sum(node1_sort[0:C])
  ans = sum(A) - sum(node_sort[B:])*X - C_sum

print(ans)