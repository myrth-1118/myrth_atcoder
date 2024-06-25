H = int(input())
num = 1
ans = 0

while H != 0:
  ans += num
  num *= 2
  H //= 2

print(ans)