N = int(input())
a = list(map(int,input().split()))
flag = [False]*8
num = 0
flag_num = 0

for i in a:
  point = i // 400
  if point < 8:
    flag[point] = True
  else:
    num += 1

for i in flag:
  if i:
    flag_num += 1

if flag_num == 0:
  print(1, num)
  exit()

print(flag_num, flag_num + num)