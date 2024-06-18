N = int(input())
ans = []

num = 1
while N > 5**num:
  num += 1

for i in range(num - 1,-1,-1):
  for j in range(1,6):
    if N > j*5**i:
      continue
    else:
      ans.append(str((2*(j - 1))))
      N -= (j - 1)*5**i
      break

print(''.join(ans))