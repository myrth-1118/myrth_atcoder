from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
num = defaultdict(int)
ans = 0

for i in A:
  a = i % 200
  num[a] += 1

for i in num:
  ans += num[i]*(num[i] - 1) // 2

print(ans)