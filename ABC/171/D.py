from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
node = defaultdict(int)
ans = 0

for i in A:
  node[i] += 1
  ans += i

for _ in range(Q):
  B, C = map(int,input().split())
  node[C] += node[B]
  ans += node[B]*(C - B)
  node[B] = 0
  
  print(ans)