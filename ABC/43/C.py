N = int(input())
a = list(map(int,input().split()))
ans = 0
x = round(sum(a) / N)

for i in a:
  ans += (x - i)**2

print(ans)