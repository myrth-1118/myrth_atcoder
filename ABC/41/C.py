N = int(input())
a = list(map(int,input().split()))
ans = []

for i in range(N):
  ans.append((a[i], i + 1))

ans.sort(reverse=True)

for i in range(N):
  print(ans[i][1])