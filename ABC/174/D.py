N = int(input())
c = input()
r, w = 0, 0
ans = 0

for i in c:
  if i == 'R':
    r += 1
  else:
    w += 1

for i in range(r):
  if c[i] == 'W':
    ans += 1

print(ans)