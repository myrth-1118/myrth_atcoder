# https://atcoder.jp/contests/iroha2019-day2/tasks/iroha2019_day2_d

# UnionFind
# 最小全域木
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

N, M = map(int,input().split())
node = [[0]*4 for i in range(M)]

for i in range(M):
  A, B, C = map(int,input().split())
  node[i][0] = A - 1
  node[i][1] = B - 1
  node[i][2] = C
  node[i][3] = i

L = sorted(node,reverse=True, key=lambda x: x[2])     # Cの値でソート

uf = UnionFind(N)
ans = []

for a, b, c, i in L:
  if not uf.same(a,b):
    uf.union(a,b)
    ans.append(i + 1)

for i in sorted(ans):
  print(i)