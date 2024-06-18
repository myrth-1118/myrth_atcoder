from itertools import product     # bit全探索
N, M = map(int,input().split())
A = [list(map(int,input().split())) for i in range(M)]
K = int(input())
C = [list(map(int,input().split())) for i in range(K)]
ans = 0

for pro in product((0,1),repeat=K):   
  op = []
  num = 0
  for i in range(K): 
    if pro[i] == 1:
      op.append(C[i][0])
    else:
      op.append(C[i][1])
  
  for i in range(M):
    if A[i][0] in op and A[i][1] in op:   # AとBがopにあるとき
      num += 1
      
  ans = max(ans,num)

print(ans)