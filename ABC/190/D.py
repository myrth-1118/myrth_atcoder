N = int(input())

def make_divisors(x): # 約数列挙
  i = 1
  lower,upper = [],[]
  while i*i <= N:
    if N % i == 0:
      lower.append(i)
      if N // i != i:
        upper.append(N // i)
    i += 1
  return lower + upper[::-1]

A = make_divisors(N)
ans = 0

for i in A:       # 奇数のときカウント
  if i % 2 == 1:
    ans += 2

print(ans)