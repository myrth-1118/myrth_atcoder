# https://atcoder.jp/contests/typical90/tasks/typical90_ac
# 競プロ典型 90 問 029 ★5

# type: ignore
# 遅延セグメント木
from atcoder.lazysegtree import LazySegTree 

def op(data1, data2):       # 演算の定義
  return max(data1, data2) 

e = -1             # 単位元 op(data1, e) = data1

# lazy_upperよりdata_lowerの方が大きくなることはあり得ない
def mapping(lazy_upper, data_lower): # 上のlazyを下のdataに作用させる
                                     # 最初dataは0で、追加したレンガはlazyに入る
  if lazy_upper == -1:  # lazy_upperには既にデータが入っている
    return data_lower
  else:
    return lazy_upper

def composition(lazy_upper, lazy_lower): #上のlazyを下のlazyに作用させる
  if lazy_upper == -1:
    return lazy_lower
  else:
    return lazy_upper

_id = -1 # mapping(_id, data_lower) = data_lower

W, N = map(int,input().split())
lst = [0]*W   # 初期リスト

lazy_segtree = LazySegTree(op, e, mapping, composition, _id, lst)

for _ in range(N):
  L, R = map(int,input().split())
  L -= 1                                # Lは区間の左端のため-1する
  max_height = lazy_segtree.prod(L, R)  # LからRまでの最大値を取得
  lazy_segtree.apply(L, R, max_height + 1)  #  LからRまでにmax_height + 1を追加
  
  print(max_height + 1)