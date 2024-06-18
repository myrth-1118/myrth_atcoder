from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
num = defaultdict(int)

for i in A:
  num[i] += 1

for i in range(N):
  print(num[i + 1])