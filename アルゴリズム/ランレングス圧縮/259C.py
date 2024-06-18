# ランレングス圧縮
from itertools import groupby
S = input()
T = input()
Si= groupby(S)
Ti = groupby(T)
S_num1, S_num2, T_num1, T_num2 = [], [], [], []
ans = 'Yes'

for i, j in Si:
  a = len(list(j))
  S_num1.append(i)
  S_num2.append(a)

for i, j in Ti:
  a = len(list(j))
  T_num1.append(i)
  T_num2.append(a)

if len(S_num1) != len(T_num1): # 先にこの条件から書くと正しく実行しない
  ans = 'No'
else:
  for i in range(len(S_num1)):
    if S_num1[i] != T_num1[i]:
      ans = 'No'
    elif S_num2[i] != T_num2[i] and (S_num2[i] == 1 or S_num2[i] > T_num2[i]):
      ans = 'No'

print(ans)