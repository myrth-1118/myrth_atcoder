# 2次元座標圧縮
# 二分探索bisect
from collections import defaultdict
import bisect
N, M = map(int,input().split())
A = []
num = defaultdict(list)

for i in range(M):
  py = list(map(int,input().split())) # 同時に受け取る
  A.append(py)

for p, y in sorted(A): # sortした後の状態でnumに入れるため大小関係が保存されたまま
  num[p] += [y]

for p, y in A:
  x = bisect.bisect_right(num[p],y)
  print('%06d%06d'%(p,x))               # 0を6個埋めて表示