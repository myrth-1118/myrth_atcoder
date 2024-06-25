from collections import deque
Q = int(input())
q = deque([])

for _ in range(Q):
  n, *c = map(int,input().split())
  
  if n == 1:
    # [数字,個数]
    q.append([c[0], c[1]])
  
  else:
    ans = 0
    num = c[0]
    
    while num != 0:
      a, b = q[0][0], q[0][1]
      
      if b < num:
        ans += a*b
        num -= b
        q.popleft()
        
      elif b == num:
        ans += a*b
        num = 0
        q.popleft()
      
      else:
        ans += a*num
        q[0][1] -= num
        num = 0
        
    print(ans)