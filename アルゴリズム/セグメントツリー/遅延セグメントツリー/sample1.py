# https://atcoder.jp/contests/practice2/tasks/practice2_k
# AtCoder Library Practice Contest K

# type: ignore
# 遅延セグメント木

from atcoder.lazysegtree import LazySegTree

def op(data1, data2):
  sum1, length1 = data1
  sum2, length2 = data2
  next_sum = (sum1 + sum2) % MOD
  next_length = length1 + length2
  return (next_sum, next_length)   # dataに(区間の値の総和,対応する区間の長さ)を入れる

e = (0, 0) # opの単位元 op(data1, e) = data1
# sum + b = sum, length + c = lengthとなるような(b, c)

def mapping(lazy_upper, data_lower):   # dataの変更作業
  b, c = lazy_upper
  sum1, length1 = data_lower
  next_sum = (sum1*b + c*length1) % MOD # dataのsum1にaをかけて、dataのlength1にcをかける
  return (next_sum, length1)

_id = (1, 0) # mapping(_id, data_lower) = data_lower
# data = data*b + c = data となるような(b, c)

def composition(lazy_upper, lazy_lower): # lowerの変更作業
# lazy_lowerは子、lazy_upperは親 親から子に伝播するときの状態を考える
# lazy_lowerは既に影響を受けているもので、それに対してlazy_upperの影響を考える
# lowerはa1=b1*a1 + c1 これに対してa1 = b2*a1 + c2をする
# a1=b2(b1*a1 + c1)+c2
  b2, c2 = lazy_upper
  b1, c1 = lazy_lower
  next_b = b1 * b2 % MOD         
  next_c = (b2 * c1 + c2) % MOD
  return (next_b, next_c)

N, Q = map(int,input().split())
A = list(map(int,input().split()))
MOD = 998244353

lst = [(a, 1) for a in A]
lazy_segtree = LazySegTree(op, e, mapping, composition, _id, lst)

for _ in range(Q):
  n, *p = map(int,input().split())
  if n == 0:
    l, r, b, c = p
    lazy_segtree.apply(l, r, (b, c))
  
  else:
    l, r = p
    ans = lazy_segtree.prod(l, r)[0]
    print(ans)