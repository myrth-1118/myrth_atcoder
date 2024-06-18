N, M = map(int,input().split())
A = list(map(int,input().split()))
k = 0

for i in range(N):
  num = A[k]
  if num == i + 1:
    print(0)
    k += 1
  else:
    print(num - i - 1)