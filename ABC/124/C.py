S = input()
A = []
num = 0
ans = 0

for _ in range(len(S)):
  A.append(1 - num)
  num = 1 - num

for i in range(len(S)):
  if str(A[i]) == S[i]:
    ans += 1

if ans <= len(S) // 2:
  print(ans)
else:
  print(len(S) - ans)