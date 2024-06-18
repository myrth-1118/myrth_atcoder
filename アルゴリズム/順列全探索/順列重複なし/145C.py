# 順列全探索 順列重複なし
import itertools
import math
N = int(input())
x = []
y = []
d = 0
for i in range(N):
  xi, yi = list(map(int,input().split()))
  x.append(xi)
  y.append(yi)

arr = list(range(N))                          # (0,1,2)のようにリストで返す
arr_list = list(itertools.permutations(arr))  # 0~N-1までの順列を全パターン列挙

for ptn in arr_list:             # 1パターンごとの順番をptnとして取得
  for i in range(len(ptn) - 1):  # ptnの1番目と2番目の比較,・・・ N-1番目とN番目の比較
    a = ptn[i]
    b = ptn[i + 1]
    x1 = x[a]
    x2 = x[b]
    y1 = y[a]
    y2 = y[b]
    d += math.sqrt(((x2 - x1)**2 + (y2 - y1)**2))
    
print(d / len(arr_list))