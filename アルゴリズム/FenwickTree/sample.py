# Fenwick_Tree フェニックツリー 区間の更新、区間の合計の取得
N, Q = map(int,input().split())

class Fenwick_Tree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n
    
    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
    
    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)
    
    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

a = list(map(int,input().split()))
fw = Fenwick_Tree(N)

for i, a[i] in enumerate(a):
  fw.add(i, a[i])      # iにa[i]を追加する

for _ in range(Q):
  i, x, y = map(int,input().split())
  
  if i == 0:
    fw.add(x, y)       # xにyを追加する
  
  else:
    ans = fw.sum(x,y)  # xからy-1までの合計を返す (x,y)=(1,3) → 1と2の和を返す
    print(ans)