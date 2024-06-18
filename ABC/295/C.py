N = int(input())
A = list(map(int,input().split()))
A_sort = sorted(A)
now = -1
ans = 0

for i in A_sort:
  if now != i:
    now = i
  else:
    ans += 1
    now = -1
  
print(ans)