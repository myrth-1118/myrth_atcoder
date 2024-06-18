from collections import defaultdict
N = int(input())
node = defaultdict(int)
ans = 0

for _ in range(N):
  A = int(input())
  
  if node[A] == 0:
    node[A] = 1
    ans += 1
  else:
    node[A] = 0
    ans -= 1

print(ans)