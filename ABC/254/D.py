# 約数列挙・判定
# 素数列挙・判定(エラトステネスとの篩)
from collections import defaultdict
import math
N = int(input())
amari = []
node = defaultdict(int)
ans = 0

for i in range(1, N + 1):
  amari.append(i)

for i in range(int(math.sqrt(N)),1,-1):    # 各数字の約数の中の最大の平方数で割った値をnodeに格納
  a = i**2                                 # エラトステネスの篩と似た原理
  for j in range(1, N // a + 1):
    if amari[a*j - 1] >= a and amari[a*j - 1] % a == 0:
      amari[a*j - 1] //= a

for i in amari:
  node[i] += 1

for i in node:
  ans += node[i]**2

print(ans)