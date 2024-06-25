from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
node = defaultdict(int)

for i in A:
  node[i] += 1

num_sum = 0

for i in node:
  num_sum += node[i]*(node[i] - 1) // 2

for i in A:
  ans = num_sum - node[i]*(node[i] - 1) // 2
  if node[i] != 1:
    ans += (node[i] - 1)*(node[i] - 2) // 2
  
  print(ans)