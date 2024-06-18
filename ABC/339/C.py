N = int(input())
A = list(map(int,input().split()))
now = 0
n = 0

for i in range(N):
  if now + A[i] < 0:
    n += abs(now + A[i])
    now = 0
  else:
    now += A[i]

print(sum(A) + n)