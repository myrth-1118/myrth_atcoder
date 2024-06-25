N = int(input())
a = list(map(int,input().split()))
ans = N
num = 1

for i in a:
  if i == num:
    ans -= 1
    num += 1

if ans == N:
  print(-1)
else:
  print(ans)