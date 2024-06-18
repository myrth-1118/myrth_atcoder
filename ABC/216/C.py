N = int(input())
ans = []

num = N
for i in range(120):
  if num == 0:
    break
  elif num % 2 == 0:
    num //= 2
    ans.append('B')
  else:
    num -= 1
    ans.append('A')

ans_rev = ans[::-1]
for i in range(len(ans)):
  print(ans_rev[i],end='')