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

N = int(input())

node = [[0]*3 for _ in range(N)] # [x,y,i] iは街の比較の際に必要

for i in range(N):
  x, y = map(int,input().split())
  node[i][0] = x
  node[i][1] = y
  node[i][2] = i

a = sorted(node, key = lambda x: x[0])   # xの値でソート
b = sorted(node, key = lambda x: x[1])   # yの値でソート
Road = []  # 道のリスト [街i,街j,費用]

for i in range(N - 1):
  Road.append((a[i][2], a[i + 1][2], a[i + 1][0] - a[i][0]))  # xの距離で比較したリスト
  Road.append((b[i][2], b[i + 1][2], b[i + 1][1] - b[i][1]))  # yの距離で比較したリスト

uf = UnionFind(N)
ans = 0

for x, y, c in sorted(Road, key = lambda x: x[2]):
  if not uf.same(x, y):
    uf.union(x, y)
    ans += c

print(ans)