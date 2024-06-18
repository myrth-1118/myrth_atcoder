from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
a = sorted(set(A),reverse=True)
node = defaultdict(int)
num = 0

for i in A:
  node[i] += 1

for i in a:
  print(node[i])
  num += 1

for _ in range(N - num):
  print(0)