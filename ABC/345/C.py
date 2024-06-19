from collections import defaultdict
S = input()
node = defaultdict(int)
num = 0

for i in range(len(S)):
  node[S[i]] += 1

ans = len(S)*(len(S) - 1) // 2

for i in node:
  if node[i] >= 2:
    num = 1
    ans -= node[i]*(node[i] - 1) // 2

# 同じもの同士で交換することがある場合→初期値と同じになる
if num == 1:
  ans += 1

print(ans)