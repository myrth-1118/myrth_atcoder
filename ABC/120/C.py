S = input()
count_0 = 0
count_1 = 0
a = len(S)

for i in range(a):
  if S[i] == '0':
    count_0 += 1
  else:
    count_1 += 1

x = abs(count_0 - count_1)
print(a - x)