# ラングレンス圧縮
from itertools import groupby
S = input()
a = groupby(S)

print(len(list(a)) - 1)