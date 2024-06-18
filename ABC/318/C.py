# 二分探索bisect
import bisect
N, D, P = map(int,input().split())
F = list(map(int,input().split()))
F.sort(reverse=True)
cost = []
ans = 0

for i in range(N // D):
  a = sum(F[i*D: i*D + D])
  cost.append(a)

cost.append(sum(F[D*(N // D):]))
cost.sort()
x = bisect.bisect_left(cost,P)

ans = P*(len(cost) - x) + sum(cost[:x])

print(ans)