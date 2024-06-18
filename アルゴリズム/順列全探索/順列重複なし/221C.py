# 順列全探索 順列重複なし
import itertools
N = int(input())
S = str(N)
A = []
ans = 0

for i in range(len(S)):
  A.append(S[i])

A_list = list(itertools.permutations(A))   # 各桁の値を使った順列を返す

for ptn in A_list:
  for i in range(len(S) - 1):
    B = ptn[:i + 1]
    C = ptn[i + 1:]
    
    if B[0] != '0' and C[0] != '0':
      b = int(''.join(B))
      c = int(''.join(C))
      ans = max(ans,b*c)
  
print(ans)