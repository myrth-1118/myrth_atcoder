from collections import defaultdict
N = int(input())
node = defaultdict(int)
ans = []

for i in range(N):
  S = input()
  node[S] += 1

num= max(node.values())    # 辞書の値の最大値を取得

for i in node:
  if node[i] == num:
    ans.append(i)

ans.sort()

for i in ans:
  print(i)