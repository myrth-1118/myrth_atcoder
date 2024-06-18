N = int(input())
S = str(N)
l = len(S)
num = (l - 1) // 3
ans = 0
x = 6
i = 1

if num >= 2:
  while N >= 10**x:
    ans += (10**x - 10**(x - 3))*i
    x += 3
    i += 1
  ans += (N - 10**(x - 3) + 1)*i
  
elif num == 1:
  ans = N - 10**3 + 1

print(ans)