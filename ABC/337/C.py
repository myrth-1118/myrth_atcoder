from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
A_list = defaultdict(int)
for i in range(N):
  A_list[A[i]] = i + 1

num = -1

for i in range(N):
  check = A_list[num]
  print(check,end=' ')
  num = A_list[num]