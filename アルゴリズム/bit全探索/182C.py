# bit全探索
from itertools import product
N = list(input())
ans = 20

for pro in product((0,1),repeat=len(N)):   # 0と1から成る長さNの組み合わせの全列挙
  op = ['0']*len(N)
  num = 0
  for i in range(len(N)): 
    if pro[i] == 1:
      op[i] = N[i]
      num += 1
  
  A =''.join(op)
  if int(A) % 3 == 0:          # 3の倍数の判定
    ans = min(len(N)-num, ans) 

if ans == len(N):
  ans = -1

print(ans)