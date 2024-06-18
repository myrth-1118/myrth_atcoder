N, M = map(int,input().split())
ans = 'Yes'


for i in range(N):
  B = list(map(int,input().split()))
  if B == sorted(set(B)) and B[-1] - B[0] == M - 1 and (B[0] - 1) // 7 == (B[-1] - 1) // 7:
    if i == 0 or B[0] - num == 7:
      num = B[0]
      continue
    
    else:
      ans = 'No'
  else:
    ans = 'No'

print(ans)