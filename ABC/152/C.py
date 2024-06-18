N = int(input())
P = list(map(int,input().split()))
small = P[0]
ans = 0

for i in P:
  if small >= i:
    ans += 1
    small = min(small,i)

print(ans)