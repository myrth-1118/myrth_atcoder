N = int(input())
ans = 10**12

for i in range(1,10**6 + 1):
  if i**2 <= N:
    if N % i == 0:
      a = N // i
      ans = min(ans, a + i - 2)
  else:
    break

print(ans)