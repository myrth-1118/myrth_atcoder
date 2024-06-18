# bit全探索
from itertools import product
N, M, K = map(int,input().split())
test = []
r = []
c = []
ans = 0

for i in range(M):
  C, *A, R = list(map(str,input().split()))
  a = []
  r.append(R)
  c.append(int(C))
  
  for i in A:
    a.append(int(i))
  test.append(a)

for pro in product((0,1),repeat=N):
  num = [0]*N
  for i in range(N):
    if pro[i] == 1:
        num[i] = 1
  flag = True
  
  for i in range(M):
    count = 0
    for j in range(c[i]):
      if num[test[i][j] - 1] == 1:
        count += 1
    if count >= K and r[i] == 'x':
      flag = False
    
    elif count < K and r[i] == 'o':
      flag = False
  
  if flag:
    ans += 1
    
print(ans)