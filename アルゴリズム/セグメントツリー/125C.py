# セグメント木
import math

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

def op(x, y):
  return math.gcd(x, y)  # 最大公約数を求める

def e():
  return 0

N = int(input())
A = list(map(int,input().split()))
seg = SegTree(op, e, N, A)
ans = 0

for i in range(N):
  if seg.prod(0,i) == 0:
    x = seg.prod(i + 1, N)
    
  elif seg.prod(i + 1, N) == 0:
    x = seg.prod(0,i)
    
  else:
    x = math.gcd(seg.prod(0,i), seg.prod(i + 1, N))  # i番目の数字を除いたときの最大公約数
  
  ans = max(ans, x)

print(ans)