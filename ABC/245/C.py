from collections import deque
N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 'Yes'
q = deque([A[0],B[0]])  # deque([])の形にする

for i in range(N - 1):
  if len(q) == 0:
    ans = 'No'
    break
  check = []
  
  for j in range(len(q)):
    now = q[0]
    q.popleft()
    
    if abs(now - A[i + 1]) <= K:
      check.append(A[i + 1])
    if abs(now - B[i + 1]) <= K:
      check.append(B[i + 1])
  
  for k in set(check):
    q.append(k)

if len(q) ==  0:
  ans ='No'

print(ans)