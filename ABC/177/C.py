# 累積和
N = int(input())
A = list(map(int,input().split()))
p = [0]*(N + 1)
mod = 10**9 + 7
ans = 0

for i in range(N):
  p[i + 1] += p[i] + A[i]

for i in range(N - 1):
  ans += A[i]*(p[-1] - p[i + 1]) % mod

print(ans % mod)