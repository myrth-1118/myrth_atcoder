S = input()
ans = 0
num = 0

for i in range(len(S)):
  if S[i] == '+':
    if num == 0:
      ans += 1
    num = 0
  else:
    if S[i] == '0':
      num = 1

if num == 0:
  ans += 1

print(ans)