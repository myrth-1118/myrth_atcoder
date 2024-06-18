from collections import defaultdict
N, W = map(int,input().split())
A = defaultdict(int)
x = []
num = 0   # 重量
ans = 0   # おいしさ

for i in range(N):
  ai, bi = map(int,input().split())
  A[ai] += bi
  x.append(ai)

A_sort = set(sorted(x,reverse=True))  # 重複を避けるためにset()する

for i in A_sort:
  if A[i] + num <= W:
    num += A[i]
    ans += i*A[i]
  else:
    ans += i*(W - num)
    break

print(ans)