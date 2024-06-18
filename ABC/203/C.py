from collections import defaultdict
N, K = map(int,input().split())
P = defaultdict(int)
mura = []
temp = 0   # 現在地
money = K

for i in range(N):
  a, b = map(int,input().split())
  P[a] += b
  mura.append(int(a))

A = set(sorted(mura))

for i in A:
  if i - temp <= money:         # 現在の所持金が足りるとき
    money += temp - i + P[i]
    temp = i                    # 現在地の更新
  else:
    break

print(temp + money)