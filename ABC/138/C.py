N = int(input())
v = list(map(int,input().split()))
A = sorted(v)
A_sum = A[0] + A[1]

if N >= 3:
  for i in range(2,N):
    A_sum += A[i]*2**(i - 1)

ans = A_sum / 2**(N - 1)

print(ans)