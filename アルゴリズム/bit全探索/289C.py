# bit全探索
import itertools
N, M = map(int,input().split())
c = []
A = []
ans = 0

for i in range(M):
  C = int(input())
  a = list(map(int,input().split()))
  c.append(C)
  A.append(a)

arr_list = itertools.product((0,1), repeat=M)

for ptn in arr_list:
  check = []
  for i in range(M):
    if ptn[i] == 1:
      for j in A[i]:
        check.append(j)
  
  if len(set(check)) == N:
    ans += 1

print(ans)