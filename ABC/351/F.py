N = int(input())
A = list(map(int,input().split()))
B = sorted(A)
x, y = 0, 0

for i in range(N):
  x += B[i]*i

for i in range(N):
  y -= A[i]*(N - i - 1)

print(x + y)