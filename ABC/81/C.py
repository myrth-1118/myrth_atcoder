from collections import defaultdict
N, K = map(int,input().split())
A = list(map(int,input().split()))
node = defaultdict(int)
num = 0

for i in A:
  node[i] += 1

a = len(node)

if a <= K:
  print(0)
  exit()

for key, value in sorted(node.items(), key=lambda x: x[1]): # 辞書型をvalueでソート keyでソートする際はx[0]
  num += value
  a -= 1
  if a == K:
    print(num)
    exit()