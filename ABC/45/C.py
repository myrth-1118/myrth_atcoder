from itertools import product  # bit全探索
S = input()
ans = 0

for pro in product((0,1),repeat=len(S) - 1):
  N = S
  for i in range(len(S) - 1): 
    if pro[i] == 1:
      N = N[:len(S) - 1 - i] + '+' + N[len(S) - 1 - i:] # insert()は文字列を挿入できないため、スライスして追加する
  
  ans += eval(N)

print(ans)