S = input()
flag = True

for i in range((len(S) // 2) + 1):  # Sが回文か確認
  if S[i] != S[-(i + 1)]:
    flag = False
    break

num = 0
num1 = 0

if flag == False:
  for i in range(len(S)):   # 前についているaの確認
    if S[i] == 'a':
      num += 1
    else:
      break
    
  for i in range(len(S)):   # 後ろについているaの確認
    if S[-(i + 1)] == 'a':
      num1 += 1
    else:
      break

check = S[num : len(S) - num1]

if num < num1:
  flag = True
    
  for i in range((len(check) // 2) + 1):
    if check[i] != check[-(i + 1)]:
      flag = False
      break

if flag:
  print('Yes')
else:
  print('No')