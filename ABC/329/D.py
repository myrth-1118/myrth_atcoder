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
                self._d[self._size + i] = (v[i], i)
            for i in range(self._size - 1, 0, -1):
                self._update(i)
    
    def set(self, p, x):
        assert 0 <= p < self._n
        p += self._size
        self._d[p] = (x, p - self._size)
        for i in range(1, self._log + 1):
            self._update(p >> i)
    
    def get(self, p):
        assert 0 <= p < self._n
        return self._d[p + self._size][0]

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

# (値,座標)
# 値が同じときは座標が小さい方、値が異なるときはmax(x, y)
def op(x, y):
  if x[0] == y[0]:
    if x[1] < y[1]:
      return x
    else:
      return y
  else:
    return max(x, y)

def e():
  return (0, -1)

N, M = map(int,input().split())
A = list(map(int,input().split()))
a = [0]*N
seg = SegTree(op,e,N,a)

for i in range(M):
  p = A[i] - 1
  # pに+1する
  seg.set(p, seg.get(p) + 1)
  # 値の最大値の座標を出力
  print(seg.prod(0,N)[1] + 1)