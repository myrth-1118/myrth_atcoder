r1, c1 = map(int,input().split())
r2, c2 = map(int,input().split())
r = r2 - r1
c = c2 - c1

if r == c == 0:
  ans = 0
elif abs(r) + abs(c) <= 3:
  ans = 1
elif r == c or r == -c:
  ans = 1
elif abs(r) + abs(c) <= 6:
  ans = 2
elif (r + c) % 2 == 0:
  ans = 2
elif abs(r - c) <= 3:
  ans = 2
elif abs(r + c) <= 3:
  ans = 2
else:
  ans = 3

print(ans)