# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bf
# 競技プログラミングの鉄則　演習問題集 A58

# セグメント木
class SegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (2 * self._size)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._update(i)
    
    def set(self, p, x):
        assert 0 <= p < self._n
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)
    
    def get(self, p):
        assert 0 <= p < self._n
        return self._d[p + self._size]

    def prod(self, l, r):
        assert 0 <= l <= r <= self._n
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)
    
    def all_prod(self):
        return self._d[1]

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

def op(x, y):               # opに行いたい演算を入れる 今回は最大値が知りたいためmaxとする
  return max(x, y)

def e():                    # eには単位元を入れる
  return 0

N, Q = map(int,input().split())
A = [0]*N                   # Aにリストの初期状態を入れる
seg = SegTree(op, e, N, A)  # Nは要素数

for _ in range(Q):
  n, x, y = map(int,input().split())
  x -= 1                    # xは変更するindexまたは区間の左端なので-1する
  
  if n == 1:
    seg.set(x, y)           # setでxの値をyに更新する
  
  else:
    y -= 1                  # yはこのとき区間の右端なので-1する
    print(seg.prod(x, y))   # prodでxからy-1までの合計を返す