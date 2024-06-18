from collections import defaultdict
N, K = map(int,input().split())
c = list(map(int,input().split()))
node = defaultdict(int)
num = 0

for i in range(K):
  if node[c[i]] == 0:
    num += 1
  node[c[i]] += 1

ans = num

for i in range(N - K):
  if node[c[i]] == 1:
    num -= 1
    
  node[c[i]] -= 1
  if node[c[i + K]] == 0:
    num += 1
  
  node[c[i + K]] += 1
  ans = max(ans,num)

print(ans)