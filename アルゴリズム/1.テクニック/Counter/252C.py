import collections
N = int(input())
A = []
node = [0]*10

for _ in range(N):
  S = input()
  A.append(S)

x = list(zip(*A))

for i in range(10):
  c = collections.Counter(x[i])   # (要素:数,要素:数,・・・) keys:values
  for j in c.items():             # 一種類ずつ取得

    node[int(j[0])] = max(node[int(j[0])],10*(j[1] - 1) + i)

print(min(node))