from itertools import product  # bit全探索
N = int(input())
A = list(map(int,input().split()))
ans = 2**30

if N == 1:
  ans = A[0]
  
for pro in product((0,1),repeat=N - 1):
  P_or = A[0]
  P_xor = 0
  
  if 1 in pro:                 # 空集合がないとき
    for i in range(N - 1):
      if pro[i] == 0:          # 区切り無
        P_or = P_or | A[i + 1] # OR演算
      else:                    # 区切り有
        P_xor = P_xor ^ P_or   # XOR演算
        P_or = A[i + 1]
      
    P_xor = P_xor ^ P_or     # A[-1]を含むxor演算
    ans = min(ans,P_xor)

print(ans)