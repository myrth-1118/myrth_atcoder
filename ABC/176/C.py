N = int(input())
A = list(map(int,input().split()))
now = A[0]
ans = 0

for i in range(1,N):
  if now >= A[i]:
    ans += now - A[i]
  else:
    now = A[i]

print(ans)