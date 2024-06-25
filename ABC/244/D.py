S = list(input().split())
T = list(input().split())
num = 0

for i in range(3):
  if S[i] != T[i]:
    num += 1

if num != 2:
  print('Yes')
else:
  print('No')