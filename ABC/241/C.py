N = int(input())
S = [list(input()) for _ in range(N)]

def check(S):
  # 横の確認
  for i in range(N):
    num = 0
    for j in range(6):
      if S[i][j] == '#':
        num += 1
    if num >= 4:
        print('Yes')
        exit()
      
    for k in range(N - 6):
      if S[i][k] == '#':
        num -= 1
      if S[i][k + 6] == '#':
        num += 1
      if num >= 4:
        print('Yes')
        exit()

check(S)

# Sの転置行列をとることで縦の確認を、横の確認に変更する
x = list(zip(*S))
check(x)

for i in range(N - 5):
  for j in range(N - 5):
    # 右下斜めの確認
    num = 0
    nx, ny = i, j
    for _ in range(6):
      if S[nx][ny] == '#':
        num += 1
      nx += 1
      ny += 1
    if num >= 4:
      print('Yes')
      exit()
      
    # 右上斜めの確認
    num = 0
    nx, ny = i, j + 5
    for _ in range(6):
      if S[nx][ny] == '#':
        num += 1
      nx += 1
      ny -= 1
    if num >= 4:
      print('Yes')
      exit()

print('No')