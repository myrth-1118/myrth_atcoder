N = int(input())
H = list(map(int,input().split()))
num = 0
ans = 0

for i in range(N - 1):
  if H[i] >= H[i + 1]:
    num += 1
    ans = max(ans,num)
  else:
    num = 0
  
print(ans)