# ランレングス圧縮  連続するものの個数の数え上げ
from itertools import groupby
S = input()
a = groupby(S)           
print(len(list(a)) - 1)

# S=BBBWWのとき
# for i,j in a:
#   print(i,list(j))
# B ['B', 'B', 'B']  W ['W', 'W']
