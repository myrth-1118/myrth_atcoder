N, K = map(int,input().split())
ans = 0

for i in range(1, N + 1):
  if i >= K:
    ans += 1
  else:
    n = i
    num = 1
    while n < K:
      n *= 2
      num /= 2
    ans += num

print(ans / N)