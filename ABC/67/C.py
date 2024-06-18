# 累積和
N = int(input())
a = list(map(int,input().split()))
ans = 10**18

for i in range(N - 1):
  a[i + 1] += a[i]

for i in range(N - 1):
  ans = min(ans,abs(a[-1] - a[i]*2))

print(ans)