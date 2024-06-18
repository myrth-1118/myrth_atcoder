N, K = map(int,input().split())
H = []
num = 0

for _ in range(N):
  h = int(input())
  H.append(h)

A = sorted(H)
ans = 10**10

for i in range(N - K + 1):
  num = A[K + i - 1] - A[i]
  ans = min(ans,num)

print(ans)