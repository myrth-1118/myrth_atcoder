N = int(input())
S = input()
num = 0
ans = 0
check = 0

for i in range(N):
  if S[i] == 'o':
    num += 1
  else:
    ans = max(ans,num)
    num = 0
    check = 1
  
if check == 1:
  ans = max(ans,num)

if ans == 0:
  print(-1)
else:
  print(ans)