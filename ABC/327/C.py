A = [list(map(int,input().split())) for i in range(9)]
B = [0]*9
Flag = True

for i in range(9):  # 横の確認
  B = [0]*9
  for j in range(9):
    B[A[i][j] - 1] += 1
  if len(set(B)) != 1:
    Flag = False

for i in range(9):  # 縦の確認
  B = [0]*9
  for j in range(9):
    B[A[j][i] - 1] += 1
  if len(set(B)) != 1:
    Flag = False

for i in range(3):  # 斜めの確認
  for j in range(3):
    B = [0]*9
    for k in range(3):
      for l in range(3):
        B[A[k + i*3][l + j*3] - 1] += 1
    if len(set(B)) != 1:
      Flag = False
  
if Flag:
  print('Yes')
else:
  print('No')