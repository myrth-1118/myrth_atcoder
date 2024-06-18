N = int(input())

def A(x):
  lower,upper = [],[]
  i = 1
  while i*i <= N:
    if N % i == 0:
      lower.append(i)
      if N // i not in lower:
        upper.append(N // i)
    i += 1
  return lower + upper[::-1]

print(*A(N))