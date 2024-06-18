# 累積和
N, X = map(int,input().split())
L = list(map(int,input().split()))
ans = 1

for i in range(N - 1):
  L[i + 1] += L[i]

for i in range(N):
  if L[i] <= X:
    ans += 1
  
print(ans)