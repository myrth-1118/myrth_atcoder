from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
num = defaultdict(int)
ans = 0

for i in A:
  num[i] += 1

for i in A:
  ans += len(A) - num[i]

print(ans // 2)