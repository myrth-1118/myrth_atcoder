N = int(input())
p = []
ans = []
min_cost = 10**9
for i in range(N):
  p.append(list(map(int,input().split())) + [i + 1])

p.sort()

for a, c, i in p[::-1]:
  if c < min_cost:
    min_cost = c
    ans.append(i)

print(len(ans))
print(*sorted(ans))