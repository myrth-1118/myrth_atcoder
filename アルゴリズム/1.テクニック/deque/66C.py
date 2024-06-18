from collections import deque
n = int(input())
a = list(map(int,input().split()))
ans = deque([])

for i in range(n):
  if i % 2 == 0:
    ans.appendleft(a[i])
  else:
    ans.append(a[i])

if n % 2 == 0:
  ans.reverse()

print(*ans)