from collections import defaultdict
N = int(input())
node = defaultdict(int)
ans = 0

for _ in range(N):
  s = input()
  A = []
  for i in range(10):
    A.append(s[i])
    
  a = ''.join(sorted(A))
  node[a] += 1

for i in node:
  ans += node[i]*(node[i] - 1) // 2

print(ans)