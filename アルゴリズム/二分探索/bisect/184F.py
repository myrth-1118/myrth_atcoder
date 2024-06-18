from itertools import product  # bit全探索,半分全探索
import bisect                  # 二分探索bisect
N, T = map(int,input().split())
A = list(map(int,input().split()))
P = A[:N // 2]  # Aの前半
Q = A[N // 2:]  # Aの後半
P_sum = []
ans = 0

for pro in product((0,1),repeat=len(P)):  
  num = 0
  for i in range(len(P)): 
    if pro[i] == 1:
      num += P[i]
  P_sum.append(num)

P_sum.sort()
for pro in product((0,1),repeat=len(Q)):  
  num = 0
  for i in range(len(Q)): 
    if pro[i] == 1:
      num += Q[i]
  
  if num <=T:
    x = bisect.bisect_right(P_sum,T - num)  # PとQの和が最もTに近くなるP_sumの位置の取得
    if x == 0:
      ans = max(ans,num)
    else:
      ans =max(ans,num + P_sum[x - 1])
    
print(ans)