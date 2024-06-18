N, T = map(int,input().split())
A = list(map(int,input().split()))
num = T
A_total = 0

if T > sum(A):
  num = T % sum(A)

for i in range(N):
  A_total += A[i]
  if num < A_total:
    print(i + 1,num - A_total + A[i])
    break