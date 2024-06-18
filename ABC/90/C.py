N, M = map(int,input().split())

if N == 1 or M == 1:
  if N + M == 2:
    ans = 1
  elif N + M == 3:
    ans = 0
  else:
    ans = N + M - 3
else:
  ans = (N - 2)*(M - 2)

print(ans)